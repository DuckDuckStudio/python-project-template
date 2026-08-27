"""
# ppt

Python 包模板 https://github.com/DuckDuckStudio/python-project-template 中的示例包，
在这里添加包的介绍。
"""

from .example import add_numbers

__all__ = ["add_numbers"]

# 添加到 __all__ 可以让调用处直接使用
#
# from ppt import add_numbers
#
# 调用。
#
# -------------------------------------
#
# 不添加则使用
#
# from ppt.example import add_numbers
#
# 调用。
