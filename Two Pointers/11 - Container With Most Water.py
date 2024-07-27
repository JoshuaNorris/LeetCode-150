class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max = 0
        while l < r:
            if min(height[l], height[r]) * (r-l) > max:
                max = min(height[l], height[r]) * (r-l)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max
        