class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1

        heap = []
        for key in map:
            heapq.heappush(heap, (map[key], key))
            if len(heap) > k:
                heapq.heappop(heap)

        return [i[1] for i in heap]