class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()

        res = ["JFK"]

        adj = defaultdict(list)
        for src,d in tickets:
            adj[src].append(d)
        
        def dfs(s,res):
            if s not in adj or len(adj[s]) == 0:
                return len(res) == len(tickets)+1
            
            for i,d in enumerate(adj[s]):
                d = adj[s].pop(i)
                res.append(d)
                if dfs(d,res):
                    return True
                res.pop()
                adj[s].insert(i,d)
        dfs("JFK",res)
        return res
            
        