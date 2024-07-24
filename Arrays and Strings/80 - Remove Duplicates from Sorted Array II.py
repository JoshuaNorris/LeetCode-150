class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dict = {}
        pointer = 0
        for counter in range(len(nums)):
            if nums[counter] in dict:
                if dict[nums[counter]] == 1:
                    dict[nums[counter]] = 2
                    nums[pointer] = nums[counter]
                    pointer +=1
                else:
                    continue
            else:
                dict[nums[counter]] = 1
                nums[pointer] = nums[counter]
                pointer += 1
        return pointer