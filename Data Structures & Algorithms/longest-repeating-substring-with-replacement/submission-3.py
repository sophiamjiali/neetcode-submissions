class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Track the most frequent character observed so far. Compute
        # the longest possible substring, always including the right
        # bound. The size of the window is always the most frequent
        # character plus k replacements. 
        
        # While we can have situations where the maximum frequency 
        # does not apply to the current right-most bound, no other 
        # invalid substrings created afterwards would increase the
        # longest window we were able to originally create.

        # Moving right and encountering new characters will only 
        # strictly increrse the maximum frequency; after each 
        # iteration, the left pointer will always be updated to maintain
        # the valid window size.

        # Track the frequency of each character
        count = {}

        # Track the most frequent character so far
        longest, left, max_freq = 0, 0, 0

        # Consider the longest valid window including the right bound
        for i in range(len(s)):
            
            # Increment the frequency of the current character
            count[s[i]] = count.get(s[i], 0) + 1

            # Update the most frequent character tracker
            max_freq = max(max_freq, count[s[i]])

            # Shrink the window from the left if its too large
            while (i - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            longest = max(longest, i - left + 1)

        return longest