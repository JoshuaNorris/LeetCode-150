class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) == 0 or s is None or words is None:
            return []

        pattern_count = {}
        wordlength = len(words[0])
        concatlength = wordlength * len(words)
        result = []
        
        for word in words:
            pattern_count[word] = pattern_count.get(word, 0) + 1

        for left in range(len(s) - concatlength + 1):
            wordsseen = {}

            for right in range(len(words)):

                wordIndex = left + right * wordlength

                tempword = s[wordIndex : wordIndex + wordlength]

                if tempword not in pattern_count:
                    break
                
                wordsseen[tempword] = wordsseen.get(tempword, 0) + 1
            
                if wordsseen[tempword] > pattern_count[tempword]:
                    break
            if wordsseen == pattern_count:
                result.append(left)
        return result