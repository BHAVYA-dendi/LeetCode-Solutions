class Solution:
    def makeConnected(self, n, connections):
        if len(connections) < n - 1:
            return -1

        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        components = n

        for a, b in connections:
            pa, pb = find(a), find(b)

            if pa != pb:
                parent[pa] = pb
                components -= 1

        return components - 1
