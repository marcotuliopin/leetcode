class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1

        x = abs(x)
        rx = 0

        while x:
            rx = rx * 10 + x % 10

            x //= 10

        rx = rx * sign

        if rx < -2**31 -1 or rx > 2**31 -1:
            return 0
        return rx