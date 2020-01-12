# -*- coding: utf-8 -*-
"""
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
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

# 动态规划, 第n行的结果，在第n-1行后面补个1，然后从末尾往前算
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 0:
            return []
        if rowIndex in [0, 1]:
            return [1] * (rowIndex + 1)
        current_row = [1, 1]
        for index in range(rowIndex - 1):
            current_row.append(1)
            for i in range(len(current_row) - 2, 0, -1):
                current_row[i] = current_row[i] + current_row[i - 1]
        return current_row
