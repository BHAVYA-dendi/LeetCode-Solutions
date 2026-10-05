from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts):
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            a, b = find(a), find(b)
            if a != b:
                parent[b] = a

        for account in accounts:
            for email in account[1:]:
                parent.setdefault(email, email)

            for email in account[2:]:
                union(account[1], email)

        groups = defaultdict(list)

        for email in parent:
            groups[find(email)].append(email)

        ans = []

        for root, emails in groups.items():
            name = next(account[0] for account in accounts
                        if account[1] == root or root in account[1:])
            ans.append([name] + sorted(emails))

        return ans
