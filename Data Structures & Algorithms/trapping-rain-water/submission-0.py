class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        leftMax = 0
        rightMax = 0
        count = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] < leftMax:
                    count += leftMax - height[left]
                else:
                    leftMax = height[left]
                left += 1

            else:
                if height[right] <= rightMax:
                    count += rightMax - height[right]
                else:
                    rightMax = height[right]
                right -= 1

        return count 