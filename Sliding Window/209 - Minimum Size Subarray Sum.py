class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        currentlen = currentsum = 0
        result = 0
        
        while r <= len(nums) and l < len(nums):
            if currentsum >= target:
                if result == 0:
                    result = currentlen
                else:
                    result = min(result, currentlen)
                currentsum -= nums[l]
                currentlen -= 1
                l += 1
            else:
                if r != len(nums):
                    currentsum += nums[r]
                    currentlen += 1
                    r += 1
                else:
                    currentsum -= nums[l]
                    currentlen -= 1
                    l += 1
        return result



