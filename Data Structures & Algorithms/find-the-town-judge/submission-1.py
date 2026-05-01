class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        dic = {}
        for u,v in trust:
            if u not in dic:
                dic[u] = [0,0]
            
            if v not in dic:
                dic[v] = [0,0]

            dic[u][1] += 1
            dic[v][0] += 1
    
        for key in dic:
            if dic[key][0] == n-1 and dic[key][1] == 0:
                return key

        return -1