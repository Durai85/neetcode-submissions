class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, com = [], []
        candidates.sort()

        def dfs(i,total):   
            if total == target:
                res.append(com[:])
                return

            if total > target:
                return

            for x in range(i,len(candidates)):
                if x > i and candidates[x] == candidates[x-1]:
                    continue
                com.append(candidates[x])
                dfs(x+1,total+candidates[x])
                com.pop()
            
        dfs(0,0)
        return res