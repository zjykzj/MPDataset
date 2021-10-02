# -*- coding: utf-8 -*-

"""
@date: 2020/8/21 下午7:52
@file: build.py
@author: zj
@description: do it like this
export PYTHONPATH=/path/to/MPDataset
then
1. python tools/one_gpu_test.py
2. CUDA_VISIBLE_DEVICES=0 python tools/one_gpu_test.py
"""

from torch.utils.data import DataLoader

from mp.mp_dataset import MPDataset


def process_no_shuffle():
    # give the length of dataset, it will create a new data like list(range(length))
    ds = MPDataset(11, shuffle=False, drop_last=False)

    # Single-process loading
    print(list(DataLoader(ds, num_workers=0, batch_size=3)))
    # [tensor([0, 1, 2]), tensor([3, 4, 5]), tensor([6, 7, 8]), tensor([ 9, 10])]

    # Mult-process loading with two worker processes
    # Worker 0 fetched [3, 4].  Worker 1 fetched [5, 6].
    print(list(DataLoader(ds, num_workers=2, batch_size=3)))
    # [tensor([0, 2, 4]), tensor([1, 3, 5]), tensor([ 6,  8, 10]), tensor([7, 9])]

    # With even more workers
    print(list(DataLoader(ds, num_workers=20, batch_size=3)))
    # [tensor([0]), tensor([1]), tensor([2]), tensor([3]), tensor([4]), tensor([5]), tensor([6]), tensor([7]), tensor([8]), tensor([9]), tensor([10])]


def process_shuffle():
    # give the length of dataset, it will create a new data like list(range(length))
    ds = MPDataset(11, shuffle=True, drop_last=False)

    # Single-process loading
    print(list(DataLoader(ds, num_workers=0, batch_size=3)))
    # [tensor([8, 1, 2]), tensor([0, 6, 7]), tensor([5, 3, 4]), tensor([ 9, 10])]

    # Mult-process loading with two worker processes
    # Worker 0 fetched [3, 4].  Worker 1 fetched [5, 6].
    print(list(DataLoader(ds, num_workers=2, batch_size=3)))
    # [tensor([8, 2, 6]), tensor([1, 0, 7]), tensor([ 5,  4, 10]), tensor([3, 9])]

    # With even more workers
    print(list(DataLoader(ds, num_workers=20, batch_size=3)))
    # [tensor([8]), tensor([1]), tensor([2]), tensor([0]), tensor([6]), tensor([7]), tensor([5]), tensor([3]), tensor([4]), tensor([9]), tensor([10])]


if __name__ == '__main__':
    # note: for one-GPU/all-CPU training/testing，you should use DataLoader's drop_last param
    process_no_shuffle()
    process_shuffle()
