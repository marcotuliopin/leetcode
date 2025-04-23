class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def parse_revision(s: str) -> int:
            i = 0
            while i < len(s) and s[i] == '0':
                i += 1
            if i == len(s) or s[i] == '.':
                return 0, i + 1
            j = i + 1
            while j < len(s) and s[j] != '.':
                j += 1
            return int(s[i:j]), j + 1
            
        v1 = v2 = 0
        while v1 < len(version1) and v2 < len(version2):
            revision1, j = parse_revision(version1[v1:])
            v1 += j
            revision2, j = parse_revision(version2[v2:])
            v2 += j
            if revision1 < revision2:
                return -1
            if revision1 > revision2:
                return 1
        
        while v1 < len(version1): 
            revision1, j = parse_revision(version1[v1:])
            v1 += j
            if revision1 > 0:
                return 1
        
        while v2 < len(version2):
            revision2, j = parse_revision(version2[v2:])
            v2 += j
            if revision2 > 0:
                return -1
        return 0