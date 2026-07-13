class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)
        for w in strs:
            ordi =[0]*26
            for c in w:
                ordi[ord(c)-ord("a")] +=1
            ana[tuple(ordi)].append(w)
        return ana.values()
        

        