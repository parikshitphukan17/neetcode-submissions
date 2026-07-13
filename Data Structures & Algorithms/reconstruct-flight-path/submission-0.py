class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = defaultdict(list)
        for src,dest in tickets:
            adj[src].append(dest)
        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) +1:
                return True
            if src not in adj:
                return False
            for i,v in enumerate(list(adj[src])):
                adj[src].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                res.pop()
                adj[src].insert(i,v)
        dfs("JFK")
        return res                
            
        
        

        