class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = defaultdict(list)
        for src,des in tickets:
            adj[src].append(des)
        res = ["JFK"]
        def dfs(s):
            if s not in adj or len(adj[s]) == 0:
                return len(res) == len(tickets)+1

            for i,d in enumerate(adj[s]):
                adj[s].pop(i)
                res.append(d)
                if dfs(d):
                    return True
                res.pop()
                adj[s].insert(i,d)
        dfs("JFK")
        return res

            

        