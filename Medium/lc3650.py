import heapq

class Solution:
    def minCost(self, n, edges):
        out = [[] for _ in range(n)]
        inn = [[] for _ in range(n)]

        for u, v, w in edges:
            out[u].append((v, w))
            inn[v].append((u, w))

        INF = 10**18
        dist = [[INF, INF] for _ in range(n)]

        pq = []
        dist[0][0] = 0
        heapq.heappush(pq, (0, 0, 0))  # cost, node, used

        while pq:
            cost, u, used = heapq.heappop(pq)
            if cost > dist[u][used]:
                continue

            # Normal edges
            for v, w in out[u]:
                if dist[v][0] > cost + w:
                    dist[v][0] = cost + w
                    heapq.heappush(pq, (dist[v][0], v, 0))

            # Reversed edges (only if switch unused)
            if used == 0:
                for v, w in inn[u]:
                    if dist[v][0] > cost + 2 * w:
                        dist[v][0] = cost + 2 * w
                        heapq.heappush(pq, (dist[v][0], v, 0))

        ans = min(dist[n - 1][0], dist[n - 1][1])
        return -1 if ans >= INF else ans
s = Solution()
print(s.minCost(5, [[0,1,10],[1,2,10],[2,3,10],[3,4,10],[1,3,50]]))
# output has : 40