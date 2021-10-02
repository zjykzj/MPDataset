# -*- coding: utf-8 -*-

"""
@date: 2021/9/28 上午11:37
@file: mp_dataset.py
@author: zj
@description: 
"""

import torch
from torch.utils.data import IterableDataset
from torch.utils.data import RandomSampler, SequentialSampler

from .distributed_sampler import DistributedSampler


def build_sampler(dataset, num_gpus=1, random_sample=False, rank_id=0, drop_last=False):
    if num_gpus <= 1:
        if random_sample:
            # different work use same generator
            generator = torch.Generator()
            generator.manual_seed(int(torch.empty((), dtype=torch.int64).random_().item()))
            sampler = RandomSampler(dataset, generator=generator)
        else:
            sampler = SequentialSampler(dataset)
    else:
        shuffle = random_sample
        # using dataset.length replace dataset
        sampler = DistributedSampler(dataset.length,
                                     num_replicas=num_gpus,
                                     rank=rank_id,
                                     shuffle=shuffle,
                                     drop_last=drop_last)

    return sampler


def get_subset_data(indices):
    return [idx for idx in indices]


def shuffle_dataset(sampler, cur_epoch, is_shuffle=False):
    """"
    Shuffles the data.
    Args:
        loader (loader): data loader to perform shuffle.
        cur_epoch (int): number of the current epoch.
        is_shuffle (bool): need to shuffle the data
    """
    if not is_shuffle:
        return
    assert isinstance(
        sampler, (RandomSampler, DistributedSampler)
    ), "Sampler type '{}' not supported".format(type(sampler))
    # RandomSampler handles shuffling automatically
    if isinstance(sampler, DistributedSampler):
        # DistributedSampler shuffles data based on epoch
        sampler.set_epoch(cur_epoch)


class MPDataset(IterableDataset):

    def __init__(self, length, shuffle: bool = False,
                 num_gpus: int = 1, rank_id: int = 0, epoch: int = 0, drop_last: bool = False):
        """
        Custom Iterable Dataset class for large-scale data loading
        :param length: dataset length
        :param shuffle: is shuffle data loading
        :param num_gpus: number of used GPU, default 1
        :param rank_id: when used multiple GPU, define which rank GPU used in this process
        :param epoch: used for shuffle dataset in multi-gpus training
        :param drop_last: used for drop last dataset in multi-gpus training
        """
        super(MPDataset).__init__()
        self.length = length
        self.shuffle = shuffle

        self.rank = rank_id
        self.num_replicas = num_gpus

        self.sampler = build_sampler(self, num_gpus=self.num_replicas, random_sample=self.shuffle,
                                     rank_id=self.rank, drop_last=drop_last)
        self.set_epoch(epoch)

    def parse_file(self, label_list):
        for target in label_list:
            yield target

    def get_indices(self):
        worker_info = torch.utils.data.get_worker_info()
        if worker_info is not None:
            # in a worker process
            worker_id = worker_info.id
            # split workload
            indices = self.indices[worker_id:self.indices_length:worker_info.num_workers]
        else:
            # single-process data loading, return the full iterator
            indices = self.indices

        return indices

    def __iter__(self):
        indices = self.get_indices()
        label_list = get_subset_data(indices)

        return iter(self.parse_file(label_list))

    def __len__(self):
        return self.indices_length if self.num_replicas > 1 else self.length

    def set_epoch(self, epoch: int) -> None:
        r"""
        Sets the epoch for this sampler.

        Args:
            epoch (int): Epoch number.
        """
        shuffle_dataset(self.sampler, epoch, self.shuffle)
        self.indices = list(self.sampler)
        self.indices_length = len(self.indices)
