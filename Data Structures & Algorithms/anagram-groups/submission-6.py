class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = dict()
        for s in strs:
            sort = ''.join(sorted(s))
            if sort in group:
                group[sort].append(s)
            else:
                group[sort] = [s]

        return list(group.values())
