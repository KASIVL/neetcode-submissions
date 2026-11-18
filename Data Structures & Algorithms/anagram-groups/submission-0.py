from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #count = Counter()

        groups = {}

        for s in strs:
            new_s = "".join(sorted(s))
            if new_s in groups:
                groups[new_s].append(s)
            else:
                groups[new_s] = [s]

        ans = list(groups.values())

        return ans