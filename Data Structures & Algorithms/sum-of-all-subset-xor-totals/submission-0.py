class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        p = []
        for i in range(1,len(nums)+1):
            p.append(combinations(nums,i))
        res = 0
        for i in p:
            for j in i:
                temp = 0
                for x in j:
                    temp ^= x
                res += temp
        return res