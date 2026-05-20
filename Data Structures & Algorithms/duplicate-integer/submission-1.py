class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Initialize a set to track membership
        seen = set()

        # For each number, check if we've already seen it
        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)
        return False