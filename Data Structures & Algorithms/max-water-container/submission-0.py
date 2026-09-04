class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_water = 0

        # Perform a converging pointer sweep for max
        i, j = 0, len(heights) - 1
        while i < j:
            height_i = heights[i]
            height_j = heights[j]

            curr_water = min(height_i, height_j) * (j - i)
            max_water  = max(max_water, curr_water)

            # Move the smallest pointer
            if height_i <= height_j:
                i += 1
            else:
                j -= 1
        
        return max_water