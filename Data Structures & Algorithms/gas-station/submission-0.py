class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        total = 0
        candidate = 0
        n = len(gas)
        for i in range(n):
            diff = gas[i] - cost[i]
            tank += diff
            total += diff

            if tank < 0:
                candidate = i + 1
                tank = 0

        return -1 if total < 0 else candidate