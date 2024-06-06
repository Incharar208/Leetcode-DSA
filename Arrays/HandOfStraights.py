class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # if length of array not divisible, then grouping isnt possible
        if len(hand) % groupSize != 0:
            return False
        # counter to track the counts
        # sorting arrays
        count = Counter(hand)
        hand.sort()

        for i in hand:
            if not count[i]:
                continue
            count[i] = count[i] - 1
            for j in range(1,groupSize):
                value = i + j
                if not count[value]:
                    return False
                count[value] = count[value] - 1
        
        return True
