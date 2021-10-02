# -*- coding: utf-8 -*-

"""
@date: 2020/8/21 下午7:52
@file: build.py
@author: zj
@description: do it like this
CUDA_VISIBLE_DEVICES=0,1,2,3 python tools/multi_gpu_test.py -cfg=tools/g4.yaml
note: when need drop_last, for better optimize, both set dataset and dataloader
"""

import numpy as np
import torch
from torch.utils.data import DataLoader

from zcls.config import cfg
from zcls.util import logging
from zcls.util.distributed import init_distributed_training, get_local_rank
from zcls.util.misc import launch_job
from zcls.util.parser import parse_args, load_config

logger = logging.get_logger(__name__)

from mp.mp_dataset import MPDataset


def train(cfg):
    # Set up environment.
    init_distributed_training(cfg)
    local_rank_id = get_local_rank()

    # Set random seed from configs.
    np.random.seed(cfg.RNG_SEED + 10 * local_rank_id)
    torch.manual_seed(cfg.RNG_SEED + 10 * local_rank_id)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

    # choose length
    # # no shuffle
    # ds = MPDataset(29, shuffle=False, num_gpus=cfg.NUM_GPUS, rank_id=local_rank_id, drop_last=False)
    # dl = DataLoader(ds, num_workers=2, batch_size=3)
    # print(local_rank_id, list(dl))
    # # 0 [tensor([ 0,  8, 16]), tensor([ 4, 12, 20]), tensor([24]), tensor([28])]
    # # 1 [tensor([ 1,  9, 17]), tensor([ 5, 13, 21]), tensor([25]), tensor([0])]
    # # 2 [tensor([ 2, 10, 18]), tensor([ 6, 14, 22]), tensor([26]), tensor([1])]
    # # 3 [tensor([ 3, 11, 19]), tensor([ 7, 15, 23]), tensor([27]), tensor([2])]

    # # shuffle
    # ds = MPDataset(29, shuffle=True, num_gpus=cfg.NUM_GPUS, rank_id=local_rank_id, drop_last=False)
    # dl = DataLoader(ds, num_workers=2, batch_size=3)
    # print(local_rank_id, list(dl))
    # # 0 [tensor([ 7, 12, 21]), tensor([17, 25,  0]), tensor([16]), tensor([10])]
    # # 1 [tensor([4, 5, 1]), tensor([ 8, 20, 11]), tensor([15]), tensor([7])]
    # # 2 [tensor([22, 23,  6]), tensor([28, 27, 26]), tensor([14]), tensor([4])]
    # # 3 [tensor([19, 13,  2]), tensor([18,  3,  9]), tensor([24]), tensor([22])]

    # shuffle and drop_last
    ds = MPDataset(29, shuffle=True, num_gpus=cfg.NUM_GPUS, rank_id=local_rank_id)
    dl = DataLoader(ds, num_workers=2, batch_size=3, drop_last=True)
    print(local_rank_id, list(dl))
    # 0 [tensor([ 7, 12, 21]), tensor([17, 25,  0])]
    # 1 [tensor([4, 5, 1]), tensor([ 8, 20, 11])]
    # 3 [tensor([19, 13,  2]), tensor([18,  3,  9])]
    # 2 [tensor([22, 23,  6]), tensor([28, 27, 26])]


def main():
    args = parse_args()
    load_config(args, cfg)

    launch_job(cfg=cfg, init_method=cfg.INIT_METHOD, func=train)


if __name__ == '__main__':
    main()
