class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums) 
        for i in range(n):
            for j in range(i+1,n):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    val = nums[i] + nums[j] + nums[left] + nums[right]
                    if val == target:
                        result.append([nums[i],nums[j],nums[left],nums[right]])

                        while left < right and nums[left] == nums[left+1]: 
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        
                        left += 1
                        right -= 1
                    
                    elif val < target:
                        left += 1
                    else:
                        right -= 1

        return result