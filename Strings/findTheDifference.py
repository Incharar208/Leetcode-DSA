# converting to ascii value and finding the solution

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum1 = 0
        sum2 = 0
        for i in s :
            sum1 = sum1 + ord(i)
        for i in t :
            sum2 = sum2 + ord(i)

        extraLetter = chr(sum2 - sum1)

        return extraLetter 

# using the bitwise operator
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        value = 0
        for i in s :
            value = value ^ ord(i)
        for i in t :
            value = value ^ ord(i)

        return chr(value)    
       
        
