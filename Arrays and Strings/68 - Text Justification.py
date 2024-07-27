class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        paragraph = []
        r = 0
        line, linelength = [], 0
        while r < len(words):    
            if linelength + len(words[r]) > maxWidth:
                r -= 1
                linelength -= len(line) #Removing spaces added for counting
                if len(line) == 1:
                    paragraph.append(self.leftJustifyLine(words, maxWidth, r, line, linelength))
                else:
                    paragraph.append(self.fullJustifyLine(words, maxWidth, r, line, linelength))
                r += 1
                line = []
                linelength = 0

            elif r == len(words) - 1:
                line.append(words[r])
                linelength += len(words[r])
                paragraph.append(self.leftJustifyLine(words, maxWidth, r, line, linelength))
                r+= 1

            else:
                line.append(words[r])
                linelength += len(words[r]) + 1
                r += 1
        return paragraph

    def fullJustifyLine(self, words, maxWidth, r, line, linelength):
        result = ''
        spaces_per_space = (maxWidth - linelength) // (len(line) - 1)
        leftovers = maxWidth - linelength - (spaces_per_space * (len(line) - 1))
        for i in range(len(line) - 1):
            if leftovers > 0:
                result += self.addSpaces(line[i], spaces_per_space + 1)
                leftovers -= 1
            else:
                result += self.addSpaces(line[i], spaces_per_space)
        result += line[-1]
        return result




    def leftJustifyLine(self, words, maxWidth, r, line, linelength):
        result = ''
        for i in range(len(line)):
            if i == len(line) - 1:
                result += self.addSpaces(line[i], maxWidth - len(result) - len(line[i]))
            else:
                result += line[i] + ' '
        return result


    def addSpaces(self, word, num):
        for i in range(num):
            word += ' '
        return word
