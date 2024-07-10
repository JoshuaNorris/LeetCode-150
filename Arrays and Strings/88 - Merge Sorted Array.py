class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l = 0
        r = 0
        while l < len(nums1) - 1:
            if nums1[l] == 0:
                nums1[l] = nums2[r]
                l+=1
                r+=1
            elif nums1[l] > nums2[r]:
                self.switch_elements(l, r, nums1, nums2)
                l+=1
            else:
                l+=1
            

    def switch_elements(self, index1, index2, list1, list2):
        temp = list1[index1]
        list1[index1] = list2[index2]
        list2[index2] = temp
        self.place_left_element(index2, list2)
    
    def place_left_element(self, index, list):
        while index < len(list)-1 and list[index] > list[index + 1]:
            temp = list[index]
            list[index] = list[index + 1]
            list[index + 1] = temp
            index += 1