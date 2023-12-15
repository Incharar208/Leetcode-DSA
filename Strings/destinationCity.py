class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = []
        entries = len(paths)
        for i in range(entries):
            start.append(paths[i][0])
        
        for i in range(entries):
            if paths[i][1] not in start:
                return paths[i][1]
