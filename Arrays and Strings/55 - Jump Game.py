class Solution:
    def canJump(self, nums: List[int]) -> bool:
        spotsleft = nums[0]
        i = 1
        while spotsleft > 0 and i < len(nums):
            if nums[i] >= spotsleft:
                spotsleft = nums[i]
            else:
                spotsleft -= 1
            i += 1
        if i == len(nums):
            return True
        else:
            return False