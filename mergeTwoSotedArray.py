# -*- coding: utf-8 -*-
"""
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
"""
from typing import List


# 方法一，合并之后排序 O((m+n)log(m+n))

# 方法二，双指针, 复制一下nums1，然后遍历nums1_copy和nums2，把小的放到nums1里面
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 比较n1, n2
        # 把min(n1, n2)放到合适的位置上
        # 更新位置, 更新n1, n2
        pass

# 方法三，双指针，从大得数字开始往小的数字，把大得数字放到nums1得末尾，不需要额外的空间复制nums1
