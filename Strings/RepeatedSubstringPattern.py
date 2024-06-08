class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # let us look at the concatenation of strings solution
        # concatenating the two strings and removing the first and last character 
        # and checking if the original string is present in it or not
        newString = s + s
        n = len(newString)
        newString = newString[1:-1]
        if s in newString:
            return True
        else:
            return False
