class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
                continue
            if not stack:
                return False
            o = stack.pop()

            if o == '(' and c != ')' or o == '{' and c != '}' or o == '[' and c != ']':
                return False

        return not stack