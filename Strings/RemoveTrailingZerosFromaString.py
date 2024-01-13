class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        # to check if a number has trailing zero, that particular number will
        # be divisible by 10
        number = int(num)
        j = 0
        if number % 10 == 0:
            reverseNum = num[::-1]
            # if the number is 0 then we move j
            for i in reverseNum:
                if i == '0':
                    j = j + 1
                # when we encounter a number other than 0 we stop moving the j pointer
                # and consider the. number that that point to the end
                # and reverse the number and return it
                else:
                    finalNum = reverseNum[j:]
                    finalNum = finalNum[::-1]
                    return finalNum
        else:
            return num
