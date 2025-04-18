class Solution:
    def myAtoi(self, s: str) -> int:
        def make_return(num: int, signal: int) -> int:
            num = num * signal
            if num < -2**31:
                return -2**31
            if num > 2**31 - 1:
                return 2**31 - 1
            return num

        s = s.strip()
        if not s:
            return 0

        signal = -1 if s[0] == '-' else 1
        if s[0] == '-' or s[0] == '+':
            s = s[1:]
        
        num = 0
        for char in s:
            if not char.isdigit():
                return make_return(num, signal)
            num = num * 10 + int(char)
        return make_return(num, signal)