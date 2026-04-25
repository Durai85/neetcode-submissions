class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            seen.add(num)
        
        m = 0
        for num in seen:
            count = 1
            if num-1 not in seen and num + 1 in seen:
                temp = num
                while temp + 1 in seen:
                    temp += 1
                    count += 1
            m = max(m,count)

        return m