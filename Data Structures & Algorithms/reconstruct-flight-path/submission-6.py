class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = defaultdict(list)
        for src,dest in tickets:
            adj[src].append(dest)
        res = ["JFK"]
        N = len(tickets)
        def dfs(src):
            if src not in adj or len(adj[src]) == 0:
                return len(res) == N+1
            for i in range(len(adj[src])):
                dest = adj[src].pop(i)
                res.append(dest)
                if dfs(dest):
                    return True
                res.pop()
                adj[src].insert(i,dest)
        dfs("JFK")
        return res

        