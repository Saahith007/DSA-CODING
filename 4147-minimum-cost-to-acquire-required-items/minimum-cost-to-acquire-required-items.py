class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        res1 = 0
        res2 = 0
        res3 = 0
        best1 = min(cost1,costBoth)
        best2 = min(cost1,costBoth)

        res1 = (need1 * cost1) + (need2 * cost2)

        res2 = max(need1,need2)*costBoth
        
        if need1 > need2:
            res3 = (min(need1,need2)*costBoth)+abs(need1-need2)*cost1
        else:
            res3 = (min(need1,need2)*costBoth)+abs(need1-need2)*cost2

        return min(res1,res2,res3)

        