class Solution:
    def reverseWords(self, s: str) -> str:
        s = ' '.join(s.strip().split())
        split = s.split(' ')
        l = 0
        r = len(split) - 1
        while l < r:
            temp = split[r]
            split[r] = split[l]
            split[l] = temp
            l+=1
            r-=1
        return ' '.join(split)