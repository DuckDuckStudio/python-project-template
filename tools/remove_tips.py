"""
移除项目模板中的提示的工具
"""

import re
import shutil
import sys
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import Final

from catfood.functions.print import 消息头
from colorama import Fore

ROOT: Final = Path(__file__).resolve().parent.parent
UTF8: Final = "UTF-8"


@dataclass
class TipFile:
    """
    提示文件的信息

    Attributes:
        path (str): 提示文件的相对路径
        modify (Callable[[Path], None] | None): 修改提示文件的函数，如果为 None，则表示删除提示文件
    """

    path: str
    modify: Callable[[Path], None] | None = None

    def _absolute_path(self) -> Path:
        """
        获取该提示文件的绝对路径。
        """

        return ROOT / self.path

    def _remove_tips(self) -> None:
        """
        移除该 TipFile。
        """

        print(f"{消息头.信息} 移除 {Fore.BLUE}{self.path}{Fore.RESET}")

        path = self._absolute_path()
        if path.exists():
            if path.is_file():
                path.unlink()
            elif path.is_dir():
                shutil.rmtree(path)
            else:
                raise ValueError("未知的提示文件类型")

    def _modify_tips(self) -> None:
        """
        调用指定的函数修改 TipFile。
        """

        print(f"{消息头.信息} 修改 {Fore.BLUE}{self.path}{Fore.RESET}")

        if self.modify is None:
            raise TypeError(f"提示文件 {self.path} 没有指定修改函数")

        return self.modify(self._absolute_path())

    def process(self) -> None:
        """
        处理这个提示文件。
        """

        if self.modify:
            return self._modify_tips()

        return self._remove_tips()


def _re_sub(file: Path, pattern: str | re.Pattern[str]) -> None:
    """
    删除正则匹配的内容。

    Args:
        file: 需要修改的文件
        pattern: 正则，多行模式
    """

    with open(file, "r", encoding=UTF8) as f:
        content = f.read()

    new_content = re.sub(pattern, "", content, flags=re.MULTILINE)

    if new_content == content:
        raise ValueError("修改后的内容和原文一致")

    with open(file, "w", encoding=UTF8) as f:
        f.write(new_content)


def _replace_with(file: Path, content: str) -> None:
    """
    替换指定文件的内容为指定的内容。

    Args:
        file (Path): 需要修改的文件
        content (str): 替换后的内容
    """

    with open(file, "w", encoding=UTF8) as f:
        f.write(content)


def _remove_test_tip(file: Path) -> None:
    """
    移除测试提示。

    ```yaml
    # 你可以在这里添加一些测试，以验证构建出来的东西可以用。
    ```

    Args:
        file (Path): 需要修改的文件
    """

    _re_sub(file, r"^\s+#\s你可以在这里添加一些测试，以验证构建出来的东西可以用。\n$")


def _remove_your_tip(file: Path) -> None:
    """
    移除“你的”提示。

    ```yaml
    # 你的包支持的所有 Python 版本
    # 你的包支持的所有系统
    ```

    Args:
        file (Path): 需要修改的文件
    """

    _re_sub(file, r"^\s+#\s你的.+\n")


def _replace_with_empty(file: Path) -> None:
    """
    替换指定文件的内容为空。

    Args:
        file (Path): 需要修改的文件
    """

    _replace_with(file, "")


def _clean_comment(file: Path) -> None:
    """
    清理指定文件的注释。

    Args:
        file (Path): 需要修改的文件
    """

    _re_sub(file, r"^\s*#.*\n")
    _re_sub(file, r"\s+#.*$")


def _remove_ty_exclude(file: Path) -> None:
    """
    移除 `ty check` 的 `--exclude` 参数

    Args:
        file (Path): 需要修改的文件
    """

    _re_sub(file, r'\s--exclude\s"tools"')


TIP_FILES: Final = (
    TipFile("TIPS.md"),
    TipFile("ppt/example.py"),
    TipFile("tests/test_example.py"),
    TipFile("tools/pyproject.toml"),
    TipFile("tools/remove_tips.py"),
    TipFile(".github/workflows/release_pypi.yaml", modify=_remove_test_tip),
    TipFile(".github/workflows/release_test_pypi.yaml", modify=_remove_test_tip),
    TipFile(".github/workflows/tests.yaml", modify=_remove_your_tip),
    TipFile(".github/workflows/lint.yaml", modify=_remove_ty_exclude),
    TipFile(".github/CODEOWNERS", modify=_replace_with_empty),
    TipFile("ppt/__init__.py", modify=_replace_with_empty),
    TipFile("pyproject.toml", modify=_clean_comment),
)


def main() -> int:
    """
    入口函数
    """

    print(f"{消息头.信息} 项目目录 {Fore.BLUE}{ROOT}{Fore.RESET}")

    remove_dir_readme()
    remove_tip_files()

    return 0


def remove_tip_files() -> None:
    """
    移除提示文件。
    """

    for f in TIP_FILES:
        f.process()


def remove_dir_readme() -> None:
    """
    移除文件夹的介绍 README.md。
    """

    for readme in ROOT.rglob("README.md"):
        if readme.parent == ROOT:
            # 跳过根目录下的 README.md
            continue

        readme.unlink()


if __name__ == "__main__":
    sys.exit(main())
