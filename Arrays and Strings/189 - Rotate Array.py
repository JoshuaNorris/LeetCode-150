class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if len(nums) <= 1 or k == 0:
            return nums
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums, start, end):
        while True:
            temp = nums[end]
            nums[end] = nums[start]
            nums[start] = temp
            start += 1
            end -= 1
            if start >= end:
                break
        return nums