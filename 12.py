class Solution:
    def intToRoman(self, num: int) -> str:
        tens = ['I', 'X', 'C', 'M']
        fives = ['V', 'L', 'D']
        
        num = str(num)
        ans = ''

        for i in range(len(num)):
            pos = len(num) - i - 1

            if num[i] <= '3':
                ans += tens[pos] * int(num[i])

            elif num[i] == '4':
                ans += tens[pos] + fives[pos]
            
            elif '5' <= num[i] <= '8':
                ans += fives[pos] + tens[pos] * (int(num[i]) - 5)

            else: # num[i] == 9
                ans += tens[pos] + tens[pos + 1]
        
        return ans