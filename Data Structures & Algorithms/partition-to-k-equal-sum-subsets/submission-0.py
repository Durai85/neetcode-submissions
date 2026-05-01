class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k != 0:
            return False
        nums.sort(reverse = True)
        target = s // k
        bucket = [0] * k

        def dfs(x):
            if x == len(nums):
                # print(bucket)
                return all(b==target for b in bucket)

            for i in range(k):
                if bucket[i] + nums[x] <= target:
                    if i > 0 and bucket[i] == bucket[i-1]:
                        continue

                    bucket[i] += nums[x]
                    if dfs(x+1):
                        return True
                    
                    bucket[i] -= nums[x]

            return False

        return dfs(0)