class MapSum:

    def __init__(self):
        self.root = {}

    def insert(self, key, val):
        cur = self.root

        for ch in key:
            cur = cur.setdefault(ch, {})

        cur["#"] = val

    def sum(self, prefix):
        cur = self.root

        for ch in prefix:
            if ch not in cur:
                return 0
            cur = cur[ch]

        def dfs(node):
            total = node.get("#", 0)

            for ch, nxt in node.items():
                if ch != "#":
                    total += dfs(nxt)

            return total

        return dfs(cur)
