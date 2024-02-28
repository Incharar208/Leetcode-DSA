class Solution:
    def DivisibleByEight(self,s):
        if int(s[-3:]) % 8 == 0:
            return 1
        else:
            return -1
