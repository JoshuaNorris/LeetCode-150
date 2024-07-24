class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        prefix.append(nums[0])
        for i in range(1, len(nums)):
            prefix.append(nums[i] * prefix[i-1])
        for i in range(len(nums) - 2, -1, -1):
            nums[i] = nums[i] * nums[i + 1]
        for i in range(len(nums)):
            if i == 0:
                nums[i] = nums[i + 1]
            elif i == len(nums) - 1:
                nums[i] = prefix[i-1]
            else:
                nums[i] = nums[i+1] * prefix[i-1]
        return nums