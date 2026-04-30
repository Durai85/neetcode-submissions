class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, per = [], []

        def dfs():
            if len(per) == len(nums):
                res.append(per[:])
                return

            for x in nums:
                if x not in per:
                    per.append(x)
                    dfs()
                    per.pop()

        dfs()
        return res