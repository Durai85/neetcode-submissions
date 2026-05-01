class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, per = [], []
        used = [False] * len(nums)

        def dfs():
            if len(per) == len(nums):
                res.append(per[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                used[i] = True
                per.append(nums[i])
                dfs()
                per.pop()
                used[i] = False

        dfs()
        return res