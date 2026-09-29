class Solution:
    def isValid(self, s: str) -> bool:
        
        # Need to track parentheses using FILO approach, use a stack
        # More optimal way to track matching pairs of open-close?

        # O(n) runtime with O(n) space; as we're storing up to (n/2) symbols

        if len(s) % 2 == 1: return False

        stack = []

        for parenthesis in s:
            if parenthesis in ["(", "{", "["]:
                stack.append(parenthesis)
            else:
                if len(stack) == 0: return False
                start = stack.pop()

                if start == '(' and parenthesis != ')': return False
                elif start == '{' and parenthesis != '}': return False
                elif start == '[' and parenthesis != ']': return False

        if stack: return False
        return True
