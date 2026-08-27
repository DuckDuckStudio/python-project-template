# 一些建议

## uv
### 管理依赖
更建议你使用 `uv add` / `uv remove` / `uv sync` 命令，而不是 `uv pip ...` 命令。
在同步依赖时，建议使用 `uv sync --no-install-project`。
如果你想要安装一个依赖，但不修改 [pyproject.toml](pyproject.toml)，你可以使用 `uv pip install` 命令。
### 构建包
构建包使用这个命令：
```bash
uv build --no-sources
```

> 为什么要加 `--no-sources` 参数：https://docs.astral.sh/uv/guides/package/#building-your-package
