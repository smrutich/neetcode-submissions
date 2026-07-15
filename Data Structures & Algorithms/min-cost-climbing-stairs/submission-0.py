class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)<=2:
            return min(cost)

        target = [0] * len(cost)
        target[-1],target[-2] = cost[-1],cost[-2]
        for i in range(len(cost)-3,-1,-1):
            print(i, target,cost[i])
            target[i] = cost[i] + min(target[i+1],target[i+2])
        # print(target)
        return min(target[0],target[1])

        