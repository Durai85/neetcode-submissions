class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []

        def dfs(start, current, total):
            if total == target:
                result.append(current.copy())
                return 
            
            if total > target:
                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                current.append(nums[i])
                dfs(i+1, current, total + nums[i])
                current.pop()

            return result

        return dfs(0,[],0)