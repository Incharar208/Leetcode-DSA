# the other names of these questions are: strings rotation of each other ,
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)==len(goal): #initially checking if the length of these strings are equal or not 
            if goal in s+s: #if equal checking if the goal string present in string+string
                return True

        else:
            return False

