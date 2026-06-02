class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        Map = {0:1}
        count = 0
        prefix = 0

        for n in nums:
            prefix += n
            count += Map.get(prefix-k, 0)
            Map[prefix] = Map.get(prefix,0) + 1

        return count