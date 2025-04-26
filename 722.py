from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []

        open_block = False
        for line in source:
            if not open_block:
                new_line = ""

            start = 0
            while True:
                if open_block:
                    if (end_block := line.find("*/", start)) != -1:
                        start = end_block + 2
                        open_block = False
                        continue
                    else: break
                
                begin_comment = line.find("//", start)
                begin_block = line.find("/*", start)
                if begin_comment != -1 and (begin_block == -1 or begin_comment < begin_block):
                    new_line += line[start:begin_comment]
                    break

                if begin_block == -1:
                    new_line += line[start:]
                    break

                new_line += line[start:begin_block]
                start = begin_block + 2
                open_block = True

            if not open_block and new_line:
                ans.append(new_line)

        return ans