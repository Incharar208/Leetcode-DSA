# Time complexity: O(1)
class Solution:
    def totalMoney(self, n: int) -> int:
        if n > 7:
            count = n // 7 # to find the number of sets with 7 
            remaining = n % 7 # to find the remaning number of numbers without the 7 set
            if remaining!=0: # calculating the sum of the elements without 7 set
                middleSum = (((count+remaining)*(count+remaining+1))/2) - ((count)*(count+1)/2)
            else:
                middleSum = 0 # if set of 7 formed then there wont ne any extra numbers
            totalSum = count * 28 + ((count-1)*(count)/2) * 7 + middleSum # computing the final sum
        else:
            totalSum = (n*(n+1)/2) # if value of n lesser than 7 simply calculate the sum uptil that number

        return int(totalSum) # return the totalsum



# time complexity: O(n)
class Solution:
    def totalMoney(self, n: int) -> int:
        count = 0  # value that gets added to the list
        end = 0   # value to keep track when the value of n becomes multiple of 7 (for every monday)
        start = 1 # to keep track of the value to be increased for each subsequent monday
        answerList = [] # list that contains the answer values
        for i in range(n):
            count = count + 1
            end = end + 1
            if end % 7 == 0:
                answerList.append(count)
                start = start + 1
                count = start - 1
                end = 0
            else:
                answerList.append(count)

        return sum(answerList)
            
                
            



        
