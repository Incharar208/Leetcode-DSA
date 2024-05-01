class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        firstOccurenceOfCh = word.find('ch')
        if firstOccurenceOfCh == -1:
            return word
        finalWord = ''
        subWord = word[:firstOccurenceOfCh+1]
        subWord = subWord[::-1]
        finalWord = subWord + word[firstOccurenceOfCh+1:]

        return finalWord
