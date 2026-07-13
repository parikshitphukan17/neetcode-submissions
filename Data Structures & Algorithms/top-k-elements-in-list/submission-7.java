class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        List<Integer>[] cnt = new List[nums.length+1];
        Map<Integer,Integer> numsFreq = new HashMap<>();
        for(int n : nums){
            numsFreq.put(n,numsFreq.getOrDefault(n,0)+1);
        }
        for(Map.Entry<Integer,Integer> entry: numsFreq.entrySet()){
            var key = entry.getKey();
            var val = entry.getValue();
            if (cnt[val] == null){
                cnt[val] = new ArrayList<>();
            }
            // System.out.println(key,val);
            cnt[val].add(key);
        }
        var res = new int[k];
        int index = 0;
        for(int i = cnt.length-1;i>0 && index<k;i--){
            if(cnt[i] == null){
                continue;
            }
            for (int n : cnt[i]){
                res[index++] = n;
                if (index ==k){
                    return res;
                }
            }
        }
        return res;
    }
}
