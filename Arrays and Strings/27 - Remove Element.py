class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        r = self.trim(nums, val)
        l = 0
        if r == -1:
            return 0
        while r >= l:
            if nums[l] == val:
                nums[l] = nums[r]
                r -=1
                if nums[l] != val:
                    l+=1
            else:
                l += 1
        return l
        

    
    def trim(self, nums, val):
        last_index = len(nums) - 1
        while last_index >= 0 and nums[last_index] == val:
            last_index -= 1
        return last_index