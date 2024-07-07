class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        position = 1
        direction = 1
        for i in range(time):
            position = position + direction
            if position == n:
                direction = -1
            elif position == 1:
                direction = 1
        return position
