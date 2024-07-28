class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = currentlen = maxlen = 0
        seenletters = {}
        for r in range(len(s)):
            if s[r] not in seenletters:
                seenletters[s[r]] = 1
                currentlen += 1
                maxlen = max(currentlen, maxlen)
            else:
                while True:
                    if l == r:
                        break
                    if s[l] == s[r]:
                        l+=1
                        break
                    else:
                        currentlen -= 1
                        seenletters.pop(s[l])
                        l += 1
        return maxlen