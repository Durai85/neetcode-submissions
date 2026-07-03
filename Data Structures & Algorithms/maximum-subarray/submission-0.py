class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = globalSum = nums[0]
        for num in nums[1:]:
            curSum = max(curSum + num, num)
            globalSum = max(curSum, globalSum)

        return globalSum