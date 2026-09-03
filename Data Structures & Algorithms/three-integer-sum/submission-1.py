class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Or, use a set approach to check membership, rather than 
        # skip duplicates in the loop; however, slightly more comp.
        # overhead

        res = []
        nums.sort()

        # Iterate until there are two elements left
        for i in range(len(nums) - 2):
            
            # Protect against duplicates at the first element level
            if i > 0 and nums[i] == nums[i - 1]: continue

            # Initialize two-sum pointers
            l, r = i + 1, len(nums) - 1

            # Check each combination in the un-explored region
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]

                # Move the pointers as needed
                if curr_sum > 0: 
                    r -= 1
                elif curr_sum < 0: 
                    l += 1
                else: 
                    res.append([nums[i], nums[l], nums[r]])
                    
                    # Elements cannot match with another, skip
                    l += 1
                    r -= 1

                    # Arbitrarily skip duplicates on the left pointer
                    while nums[l] == nums[l - 1] and l < r: l += 1

        return res