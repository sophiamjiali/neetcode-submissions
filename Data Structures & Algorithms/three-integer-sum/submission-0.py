class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Sort the input list for two-sum
        nums = sorted(nums)

        # Use a set to check membership in O(1)
        n = len(nums) - 1
        result = set()

        # Iterate until there are two elements left
        for i in range(n - 1):

            # Initialize two-sum pointers
            l, r = i + 1, n

            # Check each combination in the un-explored region
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]

                # Move the pointers as needed
                if curr_sum > 0: r -= 1
                elif curr_sum < 0: l += 1
                else: 
                    row = (nums[i], nums[l], nums[r])
                    if row not in result: result.add(row)
                    l += 1

        # Convert the set of tuples into a list of lists
        return [list(x) for x in result]