class Solution:
    def romanToInt(self, s: str) -> int:
        i = 0
        total = 0
        while i < len(s):
            char = s[i]
            match char.upper():
                case 'M':
                    total += 1000
                case 'D':
                    total += 500
                case 'C':
                    if i != len(s) - 1 and s[i+1] == 'M':
                        total += 900
                        i += 1
                    elif i != len(s) - 1 and s[i+1] == 'D':
                        total += 400
                        i += 1
                    else:
                        total += 100
                case 'L':
                    total += 50
                case 'X':
                    if i != len(s) - 1 and s[i+1] == 'C':
                        total += 90
                        i += 1
                    elif i != len(s) - 1 and s[i+1] == 'L':
                        total += 40
                        i += 1
                    else:
                        total += 10
                case 'V':
                    total += 5
                case 'I':              
                    if i != len(s) - 1 and s[i+1] == 'X':
                        total += 9
                        i += 1
                    elif i != len(s) - 1 and s[i+1] == 'V':
                        total += 4
                        i += 1
                    else:
                        total += 1
            i+=1
        return total
        