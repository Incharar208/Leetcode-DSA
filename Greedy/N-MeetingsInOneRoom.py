# GFG PROBLEM


class Solution:
    def maximumMeetings(self,n,start,end):
        # if there are no schedules, there are no meetings
        if n == 0:
            return 0
        
        # combining the start and end array values, and sorting them based on the end values
        meetings = sorted(zip(start, end), key = lambda x:x[1])
        
        count = 1
        
        #initialising the runningValue to first value of the end array
        runningValue = meetings[0][1]
        
        # checking if the start value of each schedules is greater than the runningValue
        # if it is greater onky then that meeting can be scheduled
        for i in range(1,n):
            if meetings[i][0] > runningValue:
                count = count + 1
                runningValue = meetings[i][1]
                
        return count
