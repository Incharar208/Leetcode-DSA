# GFG Question
class Solution:
    def prime(self,number):
        if number == 1 :
            return False
        if number == 2 :
            return True
        isPrime = True
        squareOfNumber = int(number ** 0.5)
        
        for i in range(2,squareOfNumber+1):
            if number % i == 0:
                isPrime = False
                break
            
        return isPrime
        
    def minNumber(self, arr,n):
        sumOfArray = sum(arr)
        if self.prime(sumOfArray):
            return 0
        else:
            initialSum = sumOfArray
            while(True):
                sumOfArray = sumOfArray + 1
                if self.prime(sumOfArray):
                    return sumOfArray - initialSum
                else:
                    pass
