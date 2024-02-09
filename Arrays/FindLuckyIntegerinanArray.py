class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashMap = defaultdict(int)

        for i in arr:
            hashMap[i] = hashMap[i] + 1

        sortedHashMap = dict(sorted(hashMap.items(), key = lambda x:x[0], reverse = True))

        for key, value in sortedHashMap.items():
            if key == value:
                return key

        return -1
        
