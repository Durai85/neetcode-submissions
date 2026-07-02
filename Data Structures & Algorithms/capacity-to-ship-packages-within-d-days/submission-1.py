class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left <= right:

            mid = (left + right) // 2
            d = self.countDays(weights, mid)

            if d <= days:
                right = mid - 1
            else:
                left = mid + 1

        return left

    def countDays(self, arr, mid):
        curSum = 0
        count = 1

        for a in arr:
            if curSum + a > mid:
                count += 1
                curSum = 0
            curSum += a

        return count