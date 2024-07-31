class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # EDGE CASES
        if len(s) == 0 or len(t) == 0 or len(t) > len(s):
            return ""
        
        # VARIABLES
        lettercount, window = {}, {}

        for c in t:
            lettercount[c] = 1 + lettercount.get(c, 0)

        have, need = 0, len(lettercount)
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r] # c is the current character
            window[c] = 1 + window.get(c, 0) # updating the character count

            if c in lettercount and window[c] == lettercount[c]:
                # If c is in t, and if there is the right numebr of c's in the window
                have += 1 #have is the number of letters we have the right count for
            while have == need:
                #update result
                if (r-l + 1) < resLen:
                    res = [l, r]
                    resLen = (r-l + 1)
                
                #pop from the left of the window
                window[s[l]] -= 1
                #Check to see if we just popped an important char
                if s[l] in lettercount and window[s[l]] < lettercount[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r + 1] if resLen != float("infinity") else ""

                    
