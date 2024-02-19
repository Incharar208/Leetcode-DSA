from typing import List

class Solution:
    def maxMeetings(self, N: int, S: List[int], F: List[int]) -> List[int]:
        answerList = [] # the list to store the final indexes of the meetings that can be scheduled
        meetings = [] # to store the pairs
        
        for i in range(N):
            meetings.append([S[i], F[i], i+1])
            
        # sorting based on finish times
        meetings.sort(key=lambda x:x[1])
        
        runningValue = meetings[0][1]
        answerList.append(meetings[0][2])
        
        for i in range(1,N):
            if meetings[i][0] > runningValue:
                answerList.append(meetings[i][2])
                runningValue = meetings[i][1]
                
        answerList.sort()
        
        return answerList
