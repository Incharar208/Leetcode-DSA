class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s) and j < len(t) :
            if s[i] == t[j] :  # if the character present in s and t , increment both i and j
                i = i + 1
                j = j + 1
            else : 
                  # if character not present in s , increment t
                j = j + 1

        if i == len(s) : 
            #if i is present in the last position of the string s
            return True

        else:
            return False
