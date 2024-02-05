class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # we consider a set to store the values
        panagramSet = set()

        # checking for each letter in the sentence and adding it to the set
        for i in sentence:
            if i.isalpha():
                panagramSet.add(i)
        
        # if the len of thr set is 26 it means it contains all the letters of english alphabet
        if len(panagramSet) == 26:
            return True
        else:
            return False
