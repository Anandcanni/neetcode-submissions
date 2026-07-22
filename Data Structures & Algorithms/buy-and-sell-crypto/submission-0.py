class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = float('inf')
        max_pr = 0
        for p in prices:
            if p<min_p:
                min_p = p
            profit = p - min_p
            if profit>max_pr:
                max_pr = profit
        return max_pr