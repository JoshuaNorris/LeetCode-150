class Solution:
    def candy(self, ratings: List[int]) -> int:
        prefix = []
        for i in range(len(ratings)):

            if i == 0:
                prefix.append(1)
            
            elif ratings[i-1] < ratings[i]:
                prefix.append(prefix[i-1] + 1)

            elif ratings[i-1] >= ratings[i]:
                prefix.append(1)

        postfix = []
        for i in range(len(ratings)):
            postfix.append(1)

        for i in range(len(ratings) - 1, -1, -1):

            if i == len(ratings) - 1:
                continue
            elif ratings[i+1] < ratings[i]:
                postfix[i] = postfix[i+1] + 1
            elif ratings[i+1] >= ratings[i]:
                continue

        sum = 0
        for i in range(len(ratings)):
            sum += max(prefix[i], postfix[i])

        return sum