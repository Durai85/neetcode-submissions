class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, com = [], []

        def dfs(start, total):
            if total == target:
                res.append(com[:])
                return 
            
            if total > target:
                return 

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                com.append(nums[i])
                dfs(i+1, total + nums[i])
                com.pop()

        dfs(0,0)

        return res