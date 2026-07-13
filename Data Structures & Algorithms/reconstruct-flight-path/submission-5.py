class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = []
        tickets.sort()
        adj = defaultdict(list)
        for src,dest in tickets:
            adj[src].append(dest)

        def dfs(src):
            if src not in adj or len(adj[src]) == 0:
                return len(res) == len(tickets) +1
            for i,dest in enumerate(adj[src]):
                res.append(dest)
                adj[src].pop(i)
                if dfs(dest):
                    return True
                res.pop()
                adj[src].insert(i,dest)
        res.append("JFK")
        dfs("JFK")
        return res


            




           
        