class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        
        for s in strs:
            new = ''.join(sorted(s))
            if new in dic:
                dic[new].append(s)
            else:
                dic[new] = [s]

        result = [i for i in dic.values()]
        return result
        