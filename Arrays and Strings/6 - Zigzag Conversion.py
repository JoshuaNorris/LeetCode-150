class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = ""

        if numRows == 1:
            return s

        for i in range(numRows):
            if i == 0 or i == numRows-1:
                row_index = i
                while row_index < len(s):
                    result += s[row_index]
                    row_index += 2 * (numRows - 1)
            else:
                row_index = i
                while row_index < len(s):
                    result += s[row_index]
                    if row_index + (2 * (numRows - 1 - i)) < len(s):
                        result += s[row_index + (2 * (numRows - 1 - i))]
                    row_index += 2 * (numRows - 1)
        return result
