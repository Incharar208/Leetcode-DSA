class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMapForMagazine = defaultdict(int)
        #let us first count the occurences of each character of magazine 
        for i in magazine:
            hashMapForMagazine[i] = hashMapForMagazine[i] + 1

        # if a particular character present in ransomNote and its frequency is not zero it can be used
        for i in ransomNote:
            if i in hashMapForMagazine and hashMapForMagazine[i] != 0:
                hashMapForMagazine[i] = hashMapForMagazine[i] - 1

            else:
                return False


        return True
