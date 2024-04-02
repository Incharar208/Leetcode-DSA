class Solution:
    def extractDigits(self, x):
        number = x
        sumValue = 0
        while number != 0:
            n = number % 10 
            sumValue = sumValue + n
            number = number // 10

        return sumValue

    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        value = self.extractDigits(x)
        if x % value == 0:
            return value
        else:
            return -1
