class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        count = 0
        res = float('inf')
        n = len(nums)
        left = 0

        for right in range(n):
            count += nums[right]

            while count >= target:
                count -= nums[left]
                res = min(res, right - left + 1)
                left += 1

            
        return res if res != float('inf') else 0