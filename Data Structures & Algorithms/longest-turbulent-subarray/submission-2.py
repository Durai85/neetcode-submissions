class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1
        
        pattern = self.sign(arr[1]-arr[0])
        count = 1
        maxCount = 1
        for i in range(1,n):
            curPat = self.sign(arr[i]-arr[i-1])
            if curPat == 0:
                count = 1
            elif curPat == pattern:
                count = 2
            else:
                count += 1
            pattern = curPat
            maxCount = max(maxCount,count)

        return maxCount

    def sign(self,diff):
        return (diff > 0) - (diff < 0)