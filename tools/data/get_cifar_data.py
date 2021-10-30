# -*- coding: utf-8 -*-

"""
@date: 2021/9/24 下午5:18
@file: get_cifar_data.py
@author: zj
@description: 
"""

import os

import numpy as np
from PIL import Image
from tqdm import tqdm

from zcls.config import cfg
from zcls.config.key_word import KEY_DATASET, KEY_CLASSES, KEY_SEP
from zcls.data.datasets.build import build_dataset


def get_dataset(cfg_file, is_train=False):
    cfg.merge_from_file(cfg_file)
    dataset = build_dataset(cfg, is_train=is_train)

    return dataset


def process(dataset, dst_root):
    if not os.path.exists(dst_root):
        os.makedirs(dst_root)
    assert os.path.isdir(dst_root)

    data_list = list()
    class_list = dataset.classes
    for i, (image, target) in tqdm(enumerate(iter(dataset))):
        assert isinstance(image, Image.Image)

        cls_name = class_list[target]
        cls_dir = os.path.join(dst_root, cls_name)
        if not os.path.exists(cls_dir):
            os.makedirs(cls_dir)

        img_path = os.path.join(cls_dir, f'{i}.jpg')
        if not os.path.exists(img_path):
            image.save(img_path)

        data_list.append([img_path, str(target)])

    return data_list, class_list


def save_to_csv(data_list, csv_path):
    assert isinstance(data_list, list)
    assert not os.path.exists(csv_path)

    np.savetxt(csv_path, np.array(data_list), delimiter=KEY_SEP, fmt='%s')


if __name__ == '__main__':
    print('test ...')
    cfg_file = 'tools/data/cifar100.yaml'
    test_dataset = get_dataset(cfg_file, is_train=False)

    dst_root = 'data/cifar/imgs/test'
    data_list, class_list = process(test_dataset, dst_root)

    csv_path = os.path.join('data/cifar/test/', KEY_DATASET)
    save_to_csv(data_list, csv_path)

    csv_path = os.path.join('data/cifar/test/', KEY_CLASSES)
    save_to_csv(class_list, csv_path)

    print('train ...')
    train_dataset = get_dataset(cfg_file, is_train=True)

    dst_root = 'data/cifar/imgs/train'
    data_list, class_list = process(train_dataset, dst_root)

    csv_path = os.path.join('data/cifar/train/', KEY_DATASET)
    save_to_csv(data_list, csv_path)

    csv_path = os.path.join('data/cifar/train/', KEY_CLASSES)
    save_to_csv(class_list, csv_path)
