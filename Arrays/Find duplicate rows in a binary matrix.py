# GFG question.
class Solution:
    def repeatedRows(self, arr, m ,n):
        valueSet = set()
        answerList = []
        rowTuple = tuple()
        for i in range(m):
            rowTuple = tuple(arr[i])
            
            if rowTuple not in valueSet:
                valueSet.add(rowTuple)
            else:
                answerList.append(i)
                
        return answerList
