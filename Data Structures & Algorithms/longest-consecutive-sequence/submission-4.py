class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        count = 0
        seen = set(nums)
        for n in seen:
            if n-1 not in seen:
                count = 1
                temp = n
                while temp+1 in seen:
                    count+=1 
                    temp+=1

                result = max(count,result)

        return result