class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farther = nums[0]
        n = len(nums)
        for i in range(n):
            if farther >= n-1:
                return True
            if farther < i:
                return False
            farther = max(nums[i] + i, farther)

        return farther == n