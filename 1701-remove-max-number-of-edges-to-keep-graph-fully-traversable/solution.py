class Solution:
    def maxNumEdgesToRemove(self, n, edges):
        parentA = list(range(n + 1))
        parentB = list(range(n + 1))

        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent, a, b):
            a, b = find(parent, a), find(parent, b)

            if a == b:
                return False

            parent[a] = b
            return True

        used = 0

        # Type 3 first: Alice + Bob
        for t, a, b in edges:
            if t == 3:
                if union(parentA, a, b):
                    union(parentB, a, b)
                    used += 1

        # Type 1: Alice
        for t, a, b in edges:
            if t == 1:
                if union(parentA, a, b):
                    used += 1

        # Type 2: Bob
        for t, a, b in edges:
            if t == 2:
                if union(parentB, a, b):
                    used += 1

        # Check connectivity
        rootA = find(parentA, 1)
        rootB = find(parentB, 1)

        for i in range(2, n + 1):
            if find(parentA, i) != rootA or find(parentB, i) != rootB:
                return -1

        return len(edges) - used
