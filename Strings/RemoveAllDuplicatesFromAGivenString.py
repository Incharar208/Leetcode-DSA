class Solution:
    def removeDuplicates(self,str):
        answerString = ''
        for i in str:
            if i not in answerString:
                answerString = answerString + i
        
        return answerString
