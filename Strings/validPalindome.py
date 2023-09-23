class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()  #first converting the full string to lower Case completely
        i = 0 # beginning pointer
        j = len(s) - 1 # ending pointer
        while i < j :  # condition to keep a track of the indices
            if s[i].isalnum() : # checking for s[i] to be alphanumeric
                if s[j].isalnum() : # checking for s[j] to be alphanumeric
                    if s[i] == s[j] : # checking if s[i] and s[j] will match
                        i = i + 1
                        j = j - 1
                    else :
                        return False    

                else :
                    j = j - 1    

            else :
                i = i + 1        
        
        return True
