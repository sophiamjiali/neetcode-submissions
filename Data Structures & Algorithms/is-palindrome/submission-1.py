class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Initialize two converging pointers to opposite indices
        i, j = 0, len(s) - 1

        # Assert equality until both pointers converge
        while i < j:
            
            # Find a valid characters on either side
            while i < j and not s[i].isalnum(): i += 1
            while i < j and not s[j].isalnum(): j -= 1

            if s[i].lower() != s[j].lower(): return False
            i += 1
            j -= 1

        return True