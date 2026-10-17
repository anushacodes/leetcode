class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        # 1. make adjacency list
        # 2. dfs from source, check if dest. in it
        graph = [[] for _ in range (n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(graph, source)->bool:
            if source == destination:
                return True
            
            visited = set()
           
            def visit(node):
                 visited.add(node)                
                 for nei in graph[node]:
                    if nei == destination:
                        return True
                    if nei not in visited:
                        if visit(nei):
                            return True 

                 return False  

            return visit(source)    
        return dfs(graph, source)