class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Initialize two converging pointers to opposite indices
        i, j = 0, len(s) - 1

        # Assert equality until both pointers converge
        while i < j:
            x, y = s[i].lower(), s[j].lower()

            skip_x, skip_y = not x.isalnum(), not y.isalnum()
            
            # Skip non-alphanumeric characters
            if skip_x: i += 1
            if skip_y: j -= 1
            if skip_x or skip_y: continue

            if x != y: return False
            i += 1
            j -= 1

        return True