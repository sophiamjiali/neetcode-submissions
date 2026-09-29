class Solution:
    def isValid(self, s: str) -> bool:
        
        # Need to track parentheses using FILO approach, use a stack
        # More optimal way to track matching pairs of open-close?
            # Define a dictionary

        # O(n) runtime with O(n) space; as we're storing up to (n/2) symbols

        if len(s) % 2 == 1: return False

        mapping = { ")" : "(", "]" : "[", "}" : "{" }
        stack = []

        for x in s:
            if x in mapping:
                if stack and stack[-1] == mapping[x]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)

        return True if not stack else False