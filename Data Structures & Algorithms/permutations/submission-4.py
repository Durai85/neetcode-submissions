class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, per = [], []
        visited = set()

        def dfs():
            if len(per) == len(nums):
                res.append(per[:])
                return

            for x in nums:
                if x not in visited:
                    visited.add(x)
                    per.append(x)
                    dfs()
                    per.pop()
                    visited.remove(x)

        dfs()
        return res