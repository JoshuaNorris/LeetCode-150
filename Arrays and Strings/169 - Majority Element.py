class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        max = 0
        maxcount = 0
        for i in range(len(nums)):
            if not(nums[i] in dict):
                dict[nums[i]] = 1
            else:
                dict[nums[i]] += 1
            if dict[nums[i]] > maxcount:
                maxcount = dict[nums[i]]
                max = nums[i]
        return max