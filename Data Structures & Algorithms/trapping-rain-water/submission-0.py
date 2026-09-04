class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height) - 1

        # Compute highest prefix for each element
        prefix = [0]
        max_height = 0
        for h in height[:n]:
            max_height = max(max_height, h)
            prefix.append(max_height)

        # Compute highest suffix for each element
        suffix = [0]
        max_height = 0
        for h in height[::-1][:n]:
            max_height = max(max_height, h)
            suffix.append(max_height)

        suffix.reverse()

        total_water = 0
        for i, h in enumerate(height):
            if h > prefix[i] or h > suffix[i]: continue
            total_water += min(prefix[i], suffix[i]) - h

        return total_water



        


        