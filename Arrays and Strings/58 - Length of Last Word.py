class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        word_started = False
        i = len(s) - 1
        while i >= 0:
            char = s[i]
            match char:
                case ' ':
                    if word_started:
                        break
                case _:
                    if word_started == False:
                        word_started = True
                    length += 1
            i-=1
        return length

