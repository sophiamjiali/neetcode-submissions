class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Solution Notes:
        # - observe that the frequency of each element are bounded to the length of the list
        # - thus, the number of possible frequencies is bounded by n; use frequency as index
        # - bucket sort numbers into frequency buckets
        # - still need to count occurrences with hash map, but use buckets to extract top K

        # Count occurrences of each number
        occurrences = dict()
        for n in nums:
            occurrences[n] = occurrences.get(n, 0) + 1

        # Sort each number in the list into the frequency buckets
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in occurrences.items():
            buckets[count].append(num)

        # Traverse backwards until all K objects are extracted
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                result.append(n)
                if len(result) == k:
                    return result
                