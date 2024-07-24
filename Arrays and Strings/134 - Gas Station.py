class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        for i in range(len(gas)):
            diff.append(gas[i] - cost[i])

        sum = 0
        currentTotal = 0
        startingIndex = 0
        for i in range(len(diff)):
            currentTotal += diff[i]
            if currentTotal < 0:
                currentTotal = 0
                startingIndex = i+1
            sum += diff[i]
        if sum >= 0:
            return startingIndex
        else:
            return -1