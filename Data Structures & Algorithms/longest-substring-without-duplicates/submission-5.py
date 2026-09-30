class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # Aim for O(n) runtime and O(1) space; iterate through string once

        # Two pointers, consider next character while iterating through as right bound
        # Keep dictionary of characters and their index; check for membership. 
        # If found, move left-pointer to index excluding original position

        # Track the index of the right-most occurrence of each char
        substring = dict()
        longest, left = 0, 0

        for i in range(len(s)):

            # If a duplicate character was found
            if s[i] in substring.keys():

                # Move left pointer if the original position is in the substring
                left = max(substring[s[i]] + 1, left)
            
            # Add/update the character in the substring dictionary
            substring[s[i]] = i
            
            # Update running maximum after each iteration
            longest = max(longest, i - left + 1)

        return longest
