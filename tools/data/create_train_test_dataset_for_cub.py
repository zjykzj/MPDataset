# -*- coding: utf-8 -*-

"""
@date: 2021/9/23 上午11:18
@file: create_train_test_dataset.py
@author: zj
@description: using CUB's config files to split train/test dataset
"""

import os
import shutil

from tqdm import tqdm
from pathlib import Path
import numpy as np

from zcls.config.key_word import KEY_DATASET, KEY_CLASSES, KEY_SEP


def parse_txt_path(data_path):
    assert os.path.isfile(data_path)

    data_array = np.loadtxt(data_path, dtype=str, delimiter=' ')
    return list(data_array[:, 1])


def parse(image_path_list, split_list, src_root, dst_root):
    assert os.path.isdir(src_root), src_root
    if not os.path.exists(dst_root):
        os.makedirs(dst_root)
    assert os.path.isdir(dst_root), dst_root

    train_root = os.path.join(dst_root, 'train')
    assert not os.path.exists(train_root), train_root
    os.makedirs(train_root)

    test_root = os.path.join(dst_root, 'test')
    assert not os.path.exists(test_root), test_root
    os.makedirs(test_root)

    for image_path, flag in tqdm(zip(image_path_list, split_list)):
        cls_name, img_name = os.path.split(image_path)
        if int(flag) == 1:
            cls_dir = os.path.join(train_root, cls_name)
        else:
            cls_dir = os.path.join(test_root, cls_name)
        if not os.path.exists(cls_dir):
            os.makedirs(cls_dir)
        assert os.path.isdir(cls_dir), cls_dir

        src_image_path = os.path.join(src_root, image_path)
        assert os.path.isfile(src_image_path), src_image_path
        dst_img_path = os.path.join(cls_dir, img_name)
        shutil.copy(src_image_path, dst_img_path)


def get_classes(cls_path):
    assert os.path.isfile(cls_path), cls_path

    cls_list = np.loadtxt(cls_path, delimiter=' ', dtype=str)
    return list(cls_list[:, 1])


def get_dataset_for_mp(src_root, cls_list):
    assert os.path.isdir(src_root), src_root
    assert isinstance(cls_list, list)

    p = Path(src_root)
    images = p.rglob('*.jpg')

    data_list = list()
    for img_path in images:
        img_path = str(img_path)

        cls_name = os.path.split(os.path.split(img_path)[0])[1]
        target = cls_list.index(cls_name)

        data_list.append([img_path, str(target)])

    return data_list


def save_to_csv(data_list, csv_path):
    assert isinstance(data_list, list)
    assert not os.path.exists(csv_path)

    np.savetxt(csv_path, np.array(data_list), delimiter=KEY_SEP, fmt='%s')


if __name__ == '__main__':
    images_path = 'data/cub/CUB_200_2011/images.txt'
    image_path_list = parse_txt_path(images_path)

    train_test_split_path = 'data/cub/CUB_200_2011/train_test_split.txt'
    split_list = parse_txt_path(train_test_split_path)

    src_root = 'data/cub/CUB_200_2011/images'
    dst_root = 'data/cub/imgs'
    parse(image_path_list, split_list, src_root, dst_root)

    cls_path = 'data/cub/CUB_200_2011/classes.txt'
    cls_list = get_classes(cls_path)
    print('create train csv files')
    train_data_root = os.path.join(dst_root, 'train')
    data_list = get_dataset_for_mp(train_data_root, cls_list)

    train_dst_root = 'data/cub/train/'
    if not os.path.exists(train_dst_root):
        os.makedirs(train_dst_root)
    csv_path = os.path.join(train_dst_root, KEY_DATASET)
    save_to_csv(data_list, csv_path)
    csv_path = os.path.join('data/cub/train/', KEY_CLASSES)
    save_to_csv(cls_list, csv_path)

    print('create test csv files')
    test_data_root = os.path.join(dst_root, 'test')
    data_list = get_dataset_for_mp(test_data_root, cls_list)

    test_dst_root = 'data/cub/test/'
    if not os.path.exists(test_dst_root):
        os.makedirs(test_dst_root)
    csv_path = os.path.join(test_dst_root, KEY_DATASET)
    save_to_csv(data_list, csv_path)
    csv_path = os.path.join(test_dst_root, KEY_CLASSES)
    save_to_csv(cls_list, csv_path)
