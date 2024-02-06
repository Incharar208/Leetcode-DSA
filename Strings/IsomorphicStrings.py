class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        list1 = []
        list2 = []
        # noting down the indexes of each occurence of all the characters of each strings
        for i in s:
            list1.append(s.index(i))
        for i in t:
            list2.append(t.index(i))
        
        # if the mapping of each characters of strings match , they are considered to be isomorphic
        if list1 == list2:
            return True
        else:
            return False

        
