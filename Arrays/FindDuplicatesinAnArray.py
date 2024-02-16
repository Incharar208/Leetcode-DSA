class Solution:
    def duplicates(self, arr, n):
        duplicate = set()
        answerSet = set()
        
        for i in arr:
            if i in duplicate:
                answerSet.add(i)
                
            else:
                duplicate.add(i)
                
        if len(answerSet) == 0:
            answerSet.add(-1)
            
        result = sorted(answerSet)
        return result
