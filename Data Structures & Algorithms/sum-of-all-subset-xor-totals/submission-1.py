class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        num_or = 0
        for i in nums:
            num_or |= i

        return num_or * (1 << len(nums) - 1)