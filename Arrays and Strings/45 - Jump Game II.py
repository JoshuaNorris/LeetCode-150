class Solution:
    def jump(self, nums: List[int]) -> int:
        dict = {}
        dict[0] = 0
        for i in range(len(nums)):
            number_of_jumps = dict[i]
            for j in range(i+1, min(i+1+nums[i], len(nums))):
                if j not in dict:
                    dict[j] = number_of_jumps + 1
                elif dict[j] > number_of_jumps + 1:
                    dict[j] = number_of_jumps + 1;
        return dict[len(nums) - 1]
