class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= 2 or numRows == 1:
            return s

        ans = ''
        for row in range(numRows):
            char = 0
            for _ in range(len(s) // numRows + 1):
                if 0 <= char - row < len(s) and row < numRows - 1:
                    ans += s[char - row]
                if 0 <= char + row < len(s) and row > 0:
                    ans += s[char + row]
                char += 2 * (numRows - 1)

        return ans