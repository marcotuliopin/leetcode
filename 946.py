from typing import List


# 1 2 3 4 5
# 4 5 3 2 1

# 0 1
# 1 0
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) != len(popped):
            return False

        st = []
        p = 0

        for out in popped:
            if st and out == st[-1]:
                st.pop()
                continue
            
            if p >= len(pushed):
                return False
            if out == pushed[p]:
                p += 1
                continue

            while p < len(pushed) and pushed[p] != out:
                st.append(pushed[p])
                p += 1
            p += 1

        return not st