class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        memory = {0:1}

        for x in nums:
            prefix += x
            if prefix - k in memory:
                count += memory[prefix - k]

            memory[prefix] = memory.get(prefix,0) + 1

        return count