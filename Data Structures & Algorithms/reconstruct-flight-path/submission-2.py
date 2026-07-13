class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = defaultdict(list)
        for src,dest in tickets:
            adj[src].append(dest)

        res = ["JFK"]
        def dfs(src):
            if not adj[src]:
                return len(res) == len(tickets) +1
            
            for i,des in enumerate(adj[src]):
                newList = adj[src][:i] +adj[src][i+1:]
                adj[src] = newList
                res.append(des)
                if dfs(des):
                    return True
                res.pop()
                adj[src].insert(i,des)
        dfs("JFK")
        return res
                
        