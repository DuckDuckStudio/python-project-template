"""
ppt.example 的测试
"""

import pytest

from ppt import add_numbers


@pytest.mark.parametrize(
    ("a", "b"),
    [
        (1, 1), # 一加一，等于一 https://www.bilibili.com/video/BV1js411A71E
        (520, 1314) # 我喜欢你
    ]
)
def test_add_numbers(a: int, b: int) -> None:
    """
    测试 add_numbers 函数使用
    """

    assert add_numbers(a, b) == sum((a, b))
