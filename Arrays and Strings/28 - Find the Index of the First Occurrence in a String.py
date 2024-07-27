class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lps = self.findLPS(needle)
        nidx = 0
        hidx = 0
        while True:
            if haystack[hidx] == needle[nidx]:
                hidx +=1
                nidx +=1
            else:
                if nidx == 0:
                    hidx+=1
                else:
                    nidx = lps[nidx-1]
            
            if nidx == len(needle):
                return hidx-nidx
            if hidx == len(haystack):
                return -1



    def findLPS(self, needle):
        lps = []
        for i in range(len(needle)):
            lps.append(0)
        length = 0
        i = 0
        while True:
            if i == 0:
                i+=1
            elif needle[length] == needle[i]:
                length+=1
                lps[i] = length
                i+=1
            else:
                if length != 0:
                    length = lps[length-1]
                else:
                    lps[i] = 0
                    i+=1
            if i >=len(lps) - 1:
                break
        return lps