class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if i+1 > citations[i]:
                break
            elif i == len(citations) - 1:
                i += 1
                break
        return i
