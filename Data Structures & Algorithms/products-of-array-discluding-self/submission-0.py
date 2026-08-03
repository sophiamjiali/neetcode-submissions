class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        output = [1 for _ in range(n)]

        # Initialize output with all prefix products
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        # Multiply the output with all suffix products
        suffix = 1
        for i in reversed(list(range(n))):
            output[i] *= suffix
            suffix *= nums[i]

        return output
