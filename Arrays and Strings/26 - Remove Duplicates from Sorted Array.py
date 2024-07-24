class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 0
        dict = {}
        for counter in range(len(nums)):
            if nums[counter] in dict:
                continue
            else:
                nums[pointer] = nums[counter]
                dict[nums[pointer]] = True
                pointer += 1
        return pointer