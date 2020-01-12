# -*- coding: utf-8 -*-
"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
"""
# 股票问题的特例之一，交易次数k=1的情况，动态规划
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        考虑第i天时，持有/未持有股票的利润
        1. 第i天的时候，没有持有股票，之前就没有/之前有，第i天卖出
        2. 第i天的时候，持有股票，之前持有/之前没有，第i天买入
        d[i][<=k][0] = max(d[i-1][<=k][0], d[i-1][<=k][1] + p[i])   <=k 表示最多进行k次交易(最多买了k次)
        d[i][<=k][1] = max(d[i-1][<=k][1], d[i-1][<=k-1][0] - p[i])
        d[i] = max(d[i][0], d[i][1])
        max_profit = max(d[i]), i in [0, len(prices)]
        :param prices:
        :return:
        """
        # base 情况
        dp_i_0 = 0
        dp_i_1 = float('-inf')  #  python中的负无穷表示方法
        for price in prices:
            tmp = max(dp_i_0, dp_i_1 + price)
            dp_i_1 = max(dp_i_1, - price)
            dp_i_0 = tmp
        return dp_i_0





if __name__ == '__main__':
    s = Solution()
    prices = [7,1,5,3,6,4]
    print(s.maxProfit(prices))