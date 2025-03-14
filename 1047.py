class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        s = ''.join(stack)
        print(s)
        return s

example = 'azxxzy'
solution = Solution()
solution.removeDuplicates(example)