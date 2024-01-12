class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        # iterating through the list[str]
        for i in operations:
            # checking if the character either + or - found in the given list[str]
            if "+" in i:
                X = X + 1
            else:
                X = X - 1

        return X
