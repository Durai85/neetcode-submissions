class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        per = []
        n = len(nums)

        def dfs():
            if len(per) == n:
                res.append(per.copy())
                return

            for x in nums:
                if x not in per:
                    per.append(x)
                    dfs()
                    per.pop()     

        dfs()
        return res