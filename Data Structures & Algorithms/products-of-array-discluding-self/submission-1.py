class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProd = [0]*len(nums)
        rightProd = [0]* len(nums)

        leftProd[0] = 1
        rightProd[len(nums)-1] = 1

        for i in range(1,len(nums)):
            leftProd[i] = leftProd[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            rightProd[i] = rightProd[i+1] * nums[i+1]

        for i in range(len(nums)):
            nums[i] = rightProd[i] * leftProd[i]

        return nums