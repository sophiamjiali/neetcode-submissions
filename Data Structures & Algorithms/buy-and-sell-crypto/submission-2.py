class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Intuitively, try every possible combination in O(n^2).
        # However, redundant as you are trying everything, need to
        # find the minimum and maximum value where left < right

        # Two pointers tracking minimum and maximum value
        # One iteration through prices, updating minimum and maximum

        # Initialize left and right as indices 0 and 1; edge case where
        # right could be initialized as a value lower than left. If right
        # is updated, optionally update left to the value of right

        # Edge case, what if the length of prices is less than two?

        if len(prices) < 2: return 0
        
        buy = 0
        max_profit = 0

        for i in range(1, len(prices)):
            curr_profit = prices[i] - prices[buy]

            if curr_profit > max_profit:
                max_profit = curr_profit
            elif prices[i] < prices[buy]:
                buy = i

        return max_profit