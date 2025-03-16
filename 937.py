from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def create_key(x):
            strings = x.split(maxsplit=1)
            identifier, log = strings[0], ''.join(strings[1:])

            if any(c.isdigit() for c in log):
                return 1,

            return 0, log, identifier

        logs.sort(key=lambda x: create_key(x))
        return logs