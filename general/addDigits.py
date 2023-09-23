# this is the O(1) solution which is the most optimal solution

class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num)) == 1 :
            return num
        if num % 9 == 0 :
            return 9
        else :
            return num % 9 
