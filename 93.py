from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_num_valid(num: str) -> bool:
            if len(num) > 1 and num[0] == '0':
                return False
            if 0 <= int(num) <= 255:
                return True
            return False
            
        response = []

        def create_ips(s: str, n: int, prefix: str):
            if not s:
                return
            if n == 3 and is_num_valid(s):
                response.append(prefix + s)
                return

            for i in range(1, 4):
                if is_num_valid(s[:i]):
                    create_ips(s[i:], n + 1, prefix + s[:i] + ".")

        create_ips(s, 0, "")

        return response