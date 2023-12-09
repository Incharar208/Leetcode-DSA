# GFG QUESTION

# the solution to the number has 2 parts , part 1 is to find the sum 
# of the digits in the given number

class Solution:
    # function to find the total sum of all the digits in the given number
    def sumOfDigits(self,number):
        sumOfNumbers = 0
        while number > 0:
            remaining = number % 10
            sumOfNumbers = sumOfNumbers + remaining
            number = number // 10
            
        return sumOfNumbers
        
    # function to find whether the given number is prime or not
    def prime(self,number):
        isPrime = True
        squareOfNumber = int(number ** 0.5)
        for i in range(2,squareOfNumber+1):
            if number % i == 0:
                isPrime = False
                break
        
        return isPrime
    
    # function to find out the prime factors and its sum for the given number
    def findPrimeFactors(self,number):
        factor = 2;
        sumFinal = 0;
        while(number > 1):
            if self.prime(factor): 
                while number % factor == 0:
                    sumFinal += self.sumOfDigits(factor)
                    number //= factor;
              
          
            factor = factor + 1
     
        return sumFinal

        
    
    def smithNum(self, n):
        # first finding out if the given number is prime or not , if its a prime number 
        # we need not find the prime factors instead return 0 directly
        sumValue = 0
        sumOfPrimeFactors = 0
        if self.prime(n):
            return 0
        else:
            sumValue = self.sumOfDigits(n)
            sumOfPrimeFactors = self.findPrimeFactors(n)
            if sumValue == sumOfPrimeFactors:
                return 1
            else:
                return 0
