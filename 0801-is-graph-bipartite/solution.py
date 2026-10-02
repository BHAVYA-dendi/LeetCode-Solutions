class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        color = {}

        for start in range(len(graph)):
            if start in color:
                continue

            color[start] = 0
            stack = [start]

            while stack:
                node = stack.pop()

                for nei in graph[node]:
                    if nei not in color:
                        color[nei] = 1 - color[node]
                        stack.append(nei)
                    elif color[nei] == color[node]:
                        return False

        return True
