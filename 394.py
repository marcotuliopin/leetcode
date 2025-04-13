class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        ans = ''

        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = ''
                while s[i].isdigit():
                    num += s[i]
                    i += 1
                st.append((int(num), len(ans)))

            elif s[i].isalpha():
                ans += s[i]

            elif s[i] == ']':
                multiplier, pos = st.pop()
                ans = ans[:pos] + multiplier * ans[pos:]

            i += 1

        return ans
            
            
            