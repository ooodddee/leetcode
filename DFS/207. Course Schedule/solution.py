class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)
        
        vis = set()

        def dfs(c):
            if c in vis:
                return False
            if adj[c] == []:
                return True
            
            vis.add(c)
            for pre in adj[c]:
                if not dfs(pre):
                    return False
            vis.remove(c)
            adj[c] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True