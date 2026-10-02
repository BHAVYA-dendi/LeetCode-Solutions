class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]

        for u, v, w in times:
            graph[u].append((v, w))

        heap = [(0, k)]
        dist = {}

        while heap:
            d, node = heapq.heappop(heap)

            if node in dist:
                continue

            dist[node] = d

            for nei, weight in graph[node]:
                if nei not in dist:
                    heapq.heappush(heap, (d + weight, nei))

        return max(dist.values()) if len(dist) == n else -1
