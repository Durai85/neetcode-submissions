class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curSum = globalMax = nums[0]
        for num in nums[1:]:
            curSum = max(curSum + num, num)
            globalMax = max(curSum, globalMax)

        curSum = globalMin = nums[0]
        for num in nums[1:]:
            curSum = min(curSum + num, num)
            globalMin = min(curSum, globalMin)

        if sum(nums) == globalMin:
            return globalMax
        return max(globalMax, sum(nums)-globalMin)