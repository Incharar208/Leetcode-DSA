class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answerList = []
        hashMap1 = defaultdict(int)
        hashMap2 = defaultdict(int)
        for i in nums1:
            hashMap1[i] = hashMap1[i] + 1
        for i in nums2:
            hashMap2[i] = hashMap2[i] + 1

        for key in hashMap1:
            if key in hashMap2:
                answerList.extend([key] * min(hashMap1[key], hashMap2[key]))

        return answerList
        
