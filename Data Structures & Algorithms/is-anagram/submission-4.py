class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        # We want to track the frequency of each character, then compare
        s_dict = dict()
        for char in s: # O(n)
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1

        # Check the frequency of each character of string t
        for char in t: # O(m)
            if char not in s_dict:
                return False

            s_dict[char] -= 1
            if s_dict[char] == 0:
                s_dict.pop(char)


        return len(s_dict) == 0