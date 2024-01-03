class Solution:
    def singleElement(self, arr, N):
        value = int((sum(set(arr))*3 - (sum(arr)))/2)
        
        return value


# this is a very unique solution
# example:
# 1 , 10 , 1 , 1
# set(arr) will have [1,10]
# sum = 11
# sum * 3 = 11 * 3 = 33
# sum(arr) = 1 + 10 + 1 + 1 = 13
# 33 - 13 = 20 / 2 = 10 which occures once.
