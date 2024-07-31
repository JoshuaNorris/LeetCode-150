class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r = c = 0
        res = []
        iterationcount = 0
        totalcounted, totalcount = 0, len(matrix) * len(matrix[0])

        while True:
            while c < len(matrix[0]) - iterationcount:
                res.append(matrix[r][c])
                c += 1
                totalcounted += 1
                if totalcounted == totalcount:
                    return res
            c -= 1
            r += 1
            while r < len(matrix) - iterationcount:
                res.append(matrix[r][c])
                r += 1
                totalcounted += 1
                if totalcounted == totalcount:
                    return res
            r -= 1
            c -= 1
            while c >= 0 + iterationcount:
                res.append(matrix[r][c])
                c -= 1
                totalcounted += 1
                if totalcounted == totalcount:
                    return res
            c += 1
            r -= 1
            while r > 0 + iterationcount:
                res.append(matrix[r][c])
                r -= 1
                totalcounted += 1
                if totalcounted == totalcount:
                    return res
            c += 1
            r += 1
            iterationcount += 1


        