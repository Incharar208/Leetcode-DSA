class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # let us initialize two arrays to store the number of occurences 
        # of a particular letter in two separate arrays
        arrayForS = [0] * 26
        arrayForT = [0] * 26

        for i in s:
            arrayForS[ord(i) - ord('a')] = arrayForS[ord(i) - ord('a')] + 1

        for i in t:
            arrayForT[ord(i) - ord('a')] = arrayForT[ord(i) - ord('a')] + 1

        #counting the difference values
        count = 0
        for i in range(26):
            count = count + abs(arrayForS[i] - arrayForT[i])

        answer = count / 2

        return int(answer)
