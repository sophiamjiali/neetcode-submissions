class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Initialize input array as a hash set
        elements = set(nums)
        longest = 0

        for i in elements:
            
            # Check if the element is the start of a potential sequence
            if (i - 1) not in elements:
                curr_longest = 1
                curr = i + 1

                while curr in elements:
                    curr_longest += 1
                    curr += 1

                longest = max(longest, curr_longest)

        return longest