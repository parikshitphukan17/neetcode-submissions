class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)
        for w in strs:
            group = [0]*26
            for c in w:
                group[ord(c)-ord("a")] +=1
            ana[tuple(group)].append(w)
        return ana.values()


        