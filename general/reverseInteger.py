class Solution:
    def reverse(self, x: int) -> int:
        negative = 0
      # to check if the given number is negative
        if x < 0:
            x = x * -1
            negative = 1
        reversedNumber = 0
      # to reverse the number
        while x > 0:
            digit = x % 10
            reversedNumber = (reversedNumber * 10) + digit
            x = int(x / 10)
          # if the number is negative then multiply by -1
        if negative == 1:
            reversedNumber = reversedNumber * -1
       # to check if the number is in the 32 bit range
        maximumIntegerRange = 2 ** 31 - 1
        minimumIntegerRange = -2 ** 31
        if reversedNumber > maximumIntegerRange or reversedNumber < minimumIntegerRange:
            return 0
        else:
            return reversedNumber


        
