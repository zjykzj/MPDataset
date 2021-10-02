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

Path `mp/` provides a simple implementation. You can find the test method under path `test/`.

The complete `MPDataset` implementation has been integrated into the [zcls](https://github.com/ZJCV/ZCls) warehouse. You can view it on [mp_dataset.py](https://github.com/ZJCV/ZCls/blob/master/zcls/data/datasets/mp_dataset.py) and [MPDataset](https://zcls.readthedocs.io/en/latest/mp_dataset/)

The following are the test results based on cifar100:

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-baqh{text-align:center;vertical-align:top}
.tg .tg-c3ow{border-color:inherit;text-align:center;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-c3ow">arch</th>
    <th class="tg-c3ow">dataset</th>
    <th class="tg-c3ow">shuffle</th>
    <th class="tg-c3ow">gpu</th>
    <th class="tg-c3ow">top1</th>
    <th class="tg-c3ow">top5</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-c3ow">sfv1_3g1x</td>
    <td class="tg-c3ow">CIFAR100</td>
    <td class="tg-c3ow">no<br></td>
    <td class="tg-c3ow">1</td>
    <td class="tg-c3ow">67.300</td>
    <td class="tg-c3ow">90.440</td>
  </tr>
  <tr>
    <td class="tg-c3ow">sfv1_3g1x</td>
    <td class="tg-c3ow">MPDataset</td>
    <td class="tg-c3ow">no</td>
    <td class="tg-c3ow">1</td>
    <td class="tg-c3ow">61.760</td>
    <td class="tg-c3ow">87.130</td>
  </tr>
  <tr>
    <td class="tg-c3ow">sfv1_3g1x</td>
    <td class="tg-c3ow">GeneralDataset</td>
    <td class="tg-c3ow">no<br></td>
    <td class="tg-c3ow">1</td>
    <td class="tg-c3ow">1.150</td>
    <td class="tg-c3ow">5.010</td>
  </tr>
  <tr>
    <td class="tg-c3ow">sfv1_3g1x</td>
    <td class="tg-c3ow">CIFAR100</td>
    <td class="tg-c3ow">yes<br></td>
    <td class="tg-c3ow">1</td>
    <td class="tg-c3ow">67.620</td>
    <td class="tg-c3ow">90.880</td>
  </tr>
  <tr>
    <td class="tg-baqh">sfv1_3g1x</td>
    <td class="tg-baqh">MPDataset</td>
    <td class="tg-baqh">yes<br></td>
    <td class="tg-baqh">1</td>
    <td class="tg-baqh">62.730</td>
    <td class="tg-baqh">87.830</td>
  </tr>
  <tr>
    <td class="tg-baqh">sfv1_3g1x</td>
    <td class="tg-baqh">GeneralDataset</td>
    <td class="tg-baqh">yes</td>
    <td class="tg-baqh">1</td>
    <td class="tg-baqh">62.520</td>
    <td class="tg-baqh">87.370</td>
  </tr>
  <tr>
    <td class="tg-baqh">sfv1_3g1x</td>
    <td class="tg-baqh">CIFAR100</td>
    <td class="tg-baqh">no<br></td>
    <td class="tg-baqh">4</td>
    <td class="tg-baqh">66.410</td>
    <td class="tg-baqh">90.380</td>
  </tr>
  <tr>
    <td class="tg-baqh">sfv1_3g1x</td>
    <td class="tg-baqh">MPDataset</td>
    <td class="tg-baqh">no</td>
    <td class="tg-baqh">4</td>
    <td class="tg-baqh">60.480</td>
    <td class="tg-baqh">86.630</td>
  </tr>
  <tr>
    <td class="tg-baqh">sfv1_3g1x</td>
    <td class="tg-baqh">GeneralDataset</td>
    <td class="tg-baqh">no<br></td>
    <td class="tg-baqh">4</td>
    <td class="tg-baqh">1.000</td>
    <td class="tg-baqh">5.000</td>
  </tr>
  <tr>
    <td class="tg-baqh">sfv1_3g1x</td>
    <td class="tg-baqh">CIFAR100</td>
    <td class="tg-baqh">yes<br></td>
    <td class="tg-baqh">4</td>
    <td class="tg-baqh">66.860</td>
    <td class="tg-baqh">90.310</td>
  </tr>
  <tr>
    <td class="tg-baqh">sfv1_3g1x</td>
    <td class="tg-baqh">MPDataset</td>
    <td class="tg-baqh">yes<br></td>
    <td class="tg-baqh">4</td>
    <td class="tg-baqh">61.570</td>
    <td class="tg-baqh">86.860</td>
  </tr>
  <tr>
    <td class="tg-baqh">sfv1_3g1x</td>
    <td class="tg-baqh">GeneralDataset</td>
    <td class="tg-baqh">yes</td>
    <td class="tg-baqh">4</td>
    <td class="tg-baqh">61.570</td>
    <td class="tg-baqh">86.970</td>
  </tr>
</tbody>
</table>

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