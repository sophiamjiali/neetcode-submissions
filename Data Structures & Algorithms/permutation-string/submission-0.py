class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Return true if a permutation of s1 exists in s2

        # Use sliding window approach of len(s1) and maintain
        # a hashmap of letters to their frequency; update
        # frequencies while sliding and compare to the 
        # frequencies of s2

        # Edge case, compare lengths of strings
        if len(s2) < len(s1): return False

        # Initialize the letter frequency of s1
        target_freq = {}
        for char in s1:
            target_freq[char] = target_freq.get(char, 0) + 1

        # Initialize the pointers of the sliding window
        left, right = 0, len(s1) - 1

        # Initialize the letter frequency of s2, except the last
        window_freq = {}
        for char in s2[:right]:
            window_freq[char] = window_freq.get(char, 0) + 1

        # Continuously compare frequencies while sliding
        while right < len(s2):
            rchar = s2[right]
            lchar = s2[left]
            window_freq[rchar] = window_freq.get(rchar, 0) + 1

            print(window_freq)

            # If the window matches, return True
            if window_freq == target_freq: 
                return True

            # Else, remove the leftmost element when incrementing
            window_freq[lchar] -= 1
            if window_freq[lchar] == 0: del window_freq[lchar]

            left += 1
            right += 1

        return False
