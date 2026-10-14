class Solution:
    def validPath(self, n: int, edges: list[list[int]],
                  source: int, destination: int) -> bool:

        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node):
            if node in visited:
                return False

            if node == destination:
                return True

            visited.add(node)

            for neighbor in graph[node]:
                if dfs(neighbor):
                    return True

            return False

        return dfs(source)