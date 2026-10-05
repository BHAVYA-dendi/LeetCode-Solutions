class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        provinces = n

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    a, b = find(i), find(j)

                    if a != b:
                        parent[a] = b
                        provinces -= 1

        return provinces
