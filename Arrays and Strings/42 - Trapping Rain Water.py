class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        postfix = []
        for i in range(len(height)):
            prefix.append(0)
            postfix.append(0)
        
        localmax = height[0]
        for i in range(len(height)):
            localmax = max(localmax, height[i])
            prefix[i] = localmax

        localmax = height[len(height) - 1]
        for i in range(len(height)-1, -1, -1):
            localmax = max(localmax, height[i])
            postfix[i] = localmax

        result = 0
        for i in range(1, len(height) - 1):
            water = min(prefix[i-1], postfix[i+1]) - height[i]
            result = result + water if water > 0 else result

        return result