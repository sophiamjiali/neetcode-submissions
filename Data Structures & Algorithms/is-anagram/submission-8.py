class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Revised Solution (after submission)

        if len(s) != len(t): return False

        countS, countT = dict(), dict()

        # Count the number of occurences of each character
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # fetch, else default 0
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT

    
        # My Solution Below
        
        # # We want to track the frequency of each character, then compare
        # s_dict = dict()
        # for char in s: # O(n)
        #     if char in s_dict:
        #         s_dict[char] += 1
        #     else:
        #         s_dict[char] = 1

        # # Check the frequency of each character of string t
        # for char in t: # O(m)
        #     if char not in s_dict:
        #         return False

        #     s_dict[char] -= 1
        #     if s_dict[char] == 0:
        #         s_dict.pop(char)


        # return len(s_dict) == 0