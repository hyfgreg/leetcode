# -*- coding: utf-8 -*-
"""
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""

# 动态规划, 每一行的数字都和上一行的数字有关
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []
        ret = []
        for row in range(numRows):
            if row in [0, 1]:
                ret.append([1] * (row + 1))
                continue
            current = [1]
            last_row = ret[-1]
            for index in range(row - 1):
                current.append(last_row[index] + last_row[index + 1])
            current.append(1)
            ret.append(current)
        return ret
