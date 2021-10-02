<div align="right">
  Language:
    🇺🇸
  <a title="Chinese" href="./README.zh-CN.md">🇨🇳</a>
</div>

 <div align="center"><a title="" href="https://github.com/zjykzj/MPDataset.git"><img align="center" src="./imgs/MPDataset.png"></a></div>

<p align="center">
  «MPDataset» implements a new iterable-style dataset class for large-scale data loading.
<br>
<br>
  <a href="https://github.com/RichardLitt/standard-readme"><img src="https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square"></a>
  <a href="https://conventionalcommits.org"><img src="https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg"></a>
  <a href="http://commitizen.github.io/cz-cli/"><img src="https://img.shields.io/badge/commitizen-friendly-brightgreen.svg"></a>
</p>

Path `mp/` provides a simple implementation. You can find the test under path `tests/`.

The complete `MPDataset` implementation has been integrated into the [zcls](https://github.com/ZJCV/ZCls) warehouse. You can view it on [mp_dataset.py](https://github.com/ZJCV/ZCls/blob/master/zcls/data/datasets/mp_dataset.py) and [MPDataset](https://zcls.readthedocs.io/en/latest/mp_dataset/)

The following are the test results based on `cifar100`:

|    arch   |     dataset    | shuffle | gpu |  top1  |  top5  |
|:---------:|:--------------:|:-------:|:---:|:------:|:------:|
| sfv1_3g1x |    CIFAR100    |    no   |  1  | 67.300 | 90.440 |
| sfv1_3g1x |    MPDataset   |    no   |  1  | 61.760 | 87.130 |
| sfv1_3g1x | GeneralDataset |    no   |  1  |  1.150 |  5.010 |
| sfv1_3g1x |    CIFAR100    |   yes   |  1  | 67.620 | 90.880 |
| sfv1_3g1x |    MPDataset   |   yes   |  1  | 62.730 | 87.830 |
| sfv1_3g1x | GeneralDataset |   yes   |  1  | 62.520 | 87.370 |
| sfv1_3g1x |    CIFAR100    |    no   |  4  | 66.410 | 90.380 |
| sfv1_3g1x |    MPDataset   |    no   |  4  | 60.480 | 86.630 |
| sfv1_3g1x | GeneralDataset |    no   |  4  |  1.000 |  5.000 |
| sfv1_3g1x |    CIFAR100    |   yes   |  4  | 66.860 | 90.310 |
| sfv1_3g1x |    MPDataset   |   yes   |  4  | 61.570 | 86.860 |
| sfv1_3g1x | GeneralDataset |   yes   |  4  | 61.570 | 86.970 |

* for `dataset` item, refer to [Dataset](https://zcls.readthedocs.io/en/latest/)
  * `CIFAR100`: use the data class provided by pytorch
  * `MPDataset`: use a custom iterable data class
  * `GeneralDataset`: A wrapper class uses ImageFolder
* the complete configuration file is located at `configs/`

There is no obvious difference in accuracy for MPDataset and GeneralDataset, even better (because I created the data file according to the original data loading order, so I can get better results by disrupting the data first)

There is a very strange period, that is, using the official cifar file can always get better results

* [Why is the accuracy difference so much when I use the image data set and pytorch’s own data set directly?](https://discuss.pytorch.org/t/why-is-the-accuracy-difference-so-much-when-i-use-the-image-data-set-and-pytorchs-own-data-set-directly/92368)
* [Why is the accuracy difference so much when I use the image data set and pytorch's own data set directly?](https://stackoverflow.com/questions/63352551/why-is-the-accuracy-difference-so-much-when-i-use-the-image-data-set-and-pytorch)

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Background](#background)
- [Installation](#installation)
- [Usage](#usage)
- [Maintainers](#maintainers)
- [Thanks](#thanks)
- [Contributing](#contributing)
- [License](#license)

## Background

Based on the current big data training needs (tens of millions or even hundreds of millions), it is necessary to further optimize the training environment. In the implementation of pytoch, more data can be loaded and preprocessed synchronously through multiple processes. However, each process keeps a copy of the data, although they only need some of it.

The warehouse defines an iteratable dataset class for loading large-scale data, which can ensure that each process retains only the part of data it needs.

## Maintainers

* zhujian - *Initial work* - [zjykzj](https://github.com/zjykzj)

## Thanks

* [torch.utils.data](https://pytorch.org/docs/stable/data.html?highlight=iterabledata#torch.utils.data.IterableDataset)
* [RankDataset：超大规模数据集加载利器 [炼丹炉番外篇-1]](https://zhuanlan.zhihu.com/p/357809861)

## Contributing

Anyone's participation is welcome! Open an [issue](https://github.com/zjykzj/MPDataset/issues) or submit PRs.

Small note:

* Git submission specifications should be complied
  with [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.4/)
* If versioned, please conform to the [Semantic Versioning 2.0.0](https://semver.org) specification
* If editing the README, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme)
  specification.

## License

[Apache License 2.0](LICENSE) © 2021 zjykzj