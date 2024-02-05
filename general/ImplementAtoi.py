# GFG QUESTION

class Solution:
    def atoi(self,s):
        number = ''
        negative = False
        # to check if the given number is negative or not
        if s[0] == '-':
            negative = True
            s = s[1:]
            
        for i in s:
            if i.isdigit():
                number = number + i
            else:
                return -1
        
        if negative == True:
            return (-1 * int(number))
        else:
            return int(number)
