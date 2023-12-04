# GFG PRACTICE QUESTION
class Solution:
    def armstrongNumber (self, n):
        armstrongNumber = 0
        originalNumber = n
        while n > 0:
            digit = n % 10
            armstrongNumber = armstrongNumber + digit ** 3
            n = int( n / 10 )
            
        if originalNumber == armstrongNumber :
            return "Yes"
        else:
            return "No"
            
