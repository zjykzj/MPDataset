<div align="right">
  语言:
    🇨🇳
  <a title="英语" href="./README.md">🇺🇸</a>
</div>

 <div align="center"><a title="" href="https://github.com/zjykzj/MPDataset"><img align="center" src="./imgs/MPDataset.png"></a></div>

<p align="center">
  ««MPDataset»实现了一个全新的用于大规模数据加载的Iterable数据类
<br>
<br>
  <a href="https://github.com/RichardLitt/standard-readme"><img src="https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square"></a>
  <a href="https://conventionalcommits.org"><img src="https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg"></a>
  <a href="http://commitizen.github.io/cz-cli/"><img src="https://img.shields.io/badge/commitizen-friendly-brightgreen.svg"></a>
</p>

* 解析：[数据pipeline优化-2](https://blog.zhujian.life/posts/dcf19fb3.html)

文件夹`mp/`提供了一个简易实现，相关测试代码参看`test/`。

完整的`MPDataset`类已经集成到[zcls](https://github.com/ZJCV/ZCls)。具体路径位于[mp_dataset.py](https://github.com/ZJCV/ZCls/blob/master/zcls/data/datasets/mp_dataset.py)和[MPDataset](https://zcls.readthedocs.io/en/latest/mp_dataset/)

下面是基于`cifar100`的训练结果：

|    arch   |     dataset    | shuffle | gpu |  top1  |  top5  |
|:---------:|:--------------:|:-------:|:---:|:------:|:------:|
| sfv1_3g1x |    CIFAR100    |    no   |  1  | 69.470 | 91.350 |
| sfv1_3g1x |    MPDataset   |    no   |  1  | 67.340 | 89.560 |
| sfv1_3g1x | GeneralDataset |    no   |  1  |  1.010 |  4.960 |
| sfv1_3g1x |    CIFAR100    |   yes   |  1  | 70.350 | 91.040 |
| sfv1_3g1x |    MPDataset   |   yes   |  1  | 68.000 | 90.030 |
| sfv1_3g1x | GeneralDataset |   yes   |  1  | 68.680 | 90.660 |
| sfv1_3g1x |    CIFAR100    |    no   |  3  | 69.716 | 91.112 |
| sfv1_3g1x |    MPDataset   |    no   |  3  | 67.367 | 89.652 |
| sfv1_3g1x | GeneralDataset |    no   |  3  |  1.420 |  5.879 |
| sfv1_3g1x |    CIFAR100    |   yes   |  3  | 70.756 | 91.972 |
| sfv1_3g1x |    MPDataset   |   yes   |  3  | 68.806 | 90.252 |
| sfv1_3g1x | GeneralDataset |   yes   |  3  | 68.656 | 90.472 |

对于`dataset`字段表示含义，参见[Dataset](https://zcls.readthedocs.io/en/latest/)
  * `CIFAR100`：`Pytorch`提供的数据类；
  * `MPDataset`: 自定义的基于`Iterable`类型的数据类；
  * `GeneralDataset`: 一个包装类，内部使用`ImageFolder`。
* 完整配置文件位于`configs/`

从训练结果来看，对于`MPDataset`和`GeneralDataset`而言并没有明显差异，甚至`MPDataset`能够得到更好的结果（*因为基于原始数据加载顺序，已经进行了一次打乱操作*）。

上面也出现了一个很奇怪的现象，就是官方提供的`cifar`文件能够得到更好的效果，在网上也找到一些相关链接，有人也遇到了这个问题

* [Why is the accuracy difference so much when I use the image data set and pytorch’s own data set directly?](https://discuss.pytorch.org/t/why-is-the-accuracy-difference-so-much-when-i-use-the-image-data-set-and-pytorchs-own-data-set-directly/92368)
* [Why is the accuracy difference so much when I use the image data set and pytorch's own data set directly?](https://stackoverflow.com/questions/63352551/why-is-the-accuracy-difference-so-much-when-i-use-the-image-data-set-and-pytorch)

## 内容列表

- [内容列表](#内容列表)
- [背景](#背景)
- [主要维护人员](#主要维护人员)
- [致谢](#致谢)
- [参与贡献方式](#参与贡献方式)
- [许可证](#许可证)

## 背景

基于当前大数据训练需求(几千万甚至上亿训练数据)，有必要进一步优化训练环境。在`Pytorch`实现中，可以通过多进程同步加载的方式来预处理更多的数据。然而，每个进程都保留了全部数据的副本，尽管它们只需要其中的一部分。

对于传统的基于`Map`类型的数据类而言，`DataLoader`会在主进程中使用采样器，为子进程数据类分配相应的数据索引集合。从`v1.2`开始，`Pytorch`提供了一种新的基于`Iterable`样式的数据类 - `IterableDataset`，它可以在每个进程中定义和使用采样器。本仓库为实现大规模数据加载定义了一个基于`Iterable`类型的数据集类`MPDataset`，可以确保每个进程只保留它所需要的部分数据。

## 主要维护人员

* zhujian - *Initial work* - [zjykzj](https://github.com/zjykzj)

## 致谢

* [torch.utils.data](https://pytorch.org/docs/stable/data.html?highlight=iterabledata#torch.utils.data.IterableDataset)
* [RankDataset：超大规模数据集加载利器 [炼丹炉番外篇-1]](https://zhuanlan.zhihu.com/p/357809861)

## 参与贡献方式

欢迎任何人的参与！打开[issue](https://github.com/ZJCV/MPDataset/issues)或提交合并请求。

注意:

* `GIT`提交，请遵守[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.4/)规范
* 语义版本化，请遵守[Semantic Versioning 2.0.0](https://semver.org)规范
* `README`编写，请遵守[standard-readme](https://github.com/RichardLitt/standard-readme)规范

## 许可证

[Apache License 2.0](LICENSE) © 2021 zjykzj