class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, com = [], []

        def dfs(i,total):
            if total == target:
                res.append(com.copy())
                return

            if total >= target or i >= len(nums):
                return

            com.append(nums[i])
            dfs(i, total + nums[i])
            com.pop()
            dfs(i + 1, total)

        dfs(0,0)
        return res