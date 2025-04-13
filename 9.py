class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x1 = x
        x2 = 0
        while x:
            x2 = x2 * 10 + x % 10
            x = x // 10
        return x1 == x2