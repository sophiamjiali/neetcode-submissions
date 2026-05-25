class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Input range is < 1000 -> O(n) or better
        # - this implies a hash map/set structure for O(1) access
        #   - O(n) to construct, O(n) to loop over
        # - no sorting, thats at worst O(nlogn)
        # - must store the values in a way to check existence
        
        # Attempt #1: construct a set, for each value in list,
        #   subtract it from the target; check if the remainder
        #   is in the set
        #   - set doesn't give index

        # Attempt #2: construct a dict, number in the list is the key,
        #   index is the value; subtract each value from the target,
        #   check against the remainder; return indices

        # Attempt #3: iterate over each element in the list; if the 
        #   difference between the current element and the target is
        #   in the dictionary, return the two indices; else, add the
        #   current element and its index into the dictionary
        #   - index of the remainder must be before the current element
        #     as it strictly came from an earlier index

        dict_n = dict()
        for i in range(len(nums)):
            current = nums[i]
            remainder = target - current

            # Return the index of the remainder and the curr.
            if remainder in dict_n:
                j = dict_n[remainder]
                return [j, i]

            # Add the current element as a key-value pair
            dict_n[current] = i

        return [None, None]
