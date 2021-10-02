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

## Installation

...

## Usage

...

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