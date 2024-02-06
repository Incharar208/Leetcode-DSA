class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # let us take a dictionary which con store lists
        hashMap = defaultdict(list)
        # now we consider the sorted version of each given value and map the further sorted versions of it
        for i in strs:
            temp = tuple(sorted(i))
            hashMap[temp].append(i)
        # we return the hashMap values in the form of list
        return list(hashMap.values())
            
