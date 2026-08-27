# Python 项目模板

从来都不需要从零开始。

## 大致框架

> 这都可以自己改。

- 模板使用 [pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)。
- 模板使用 [ruff](https://docs.astral.sh/ruff/)、[ty](https://docs.astral.sh/ty/)、[pylint](https://github.com/pylint-dev/pylint) 做静态检查。
  - pylint 最大行长设置为 200 字。
- 构建使用 [uv_build](https://docs.astral.sh/uv/concepts/build-backend/#using-the-uv-build-backend) 后端。
- 构建和发布，使用 uv 通过 GitHub Action 进行可信发布（[文档](https://docs.astral.sh/uv/guides/integration/github/#publishing-to-pypi)）。
- 附带了一个 [tools](tools/) 目录，[目录中的工具](tools/README.md#remove_tipspy)可以清除模板中的提示信息和示例文件。

### 假设
- 模板假设包要求 Python 3.10 或更高版本。
- 项目假设包代码有类型注释（[py.typed](ppt/py.typed)文件）。
- 假设项目叫 `ppt`（Python Project Template），包代码位于 [ppt 目录](ppt/)，测试位于 [tests 目录](tests/)。

## 许可

此模板采用 <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0 Universal</a><img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" alt="CC 标志" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/zero.svg" alt="CC 0 标志" style="max-width: 1em;max-height:1em;margin-left: .2em;"> 许可协议。

这只是说这个模板是 CC0，不是说你用这个模板做出来的东西是 CC0。
