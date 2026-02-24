import java.util.*; 

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        
        Map<Integer, Integer> map = new HashMap<>();
        for(int x : nums) {
            map.put(x, map.getOrDefault(x, 0) + 1);
        }
        
        int uniqueCount = map.size();
        int availableSelect = nums.length / 2;
        
        if(uniqueCount > availableSelect)
            answer = availableSelect;
        else 
            answer = uniqueCount;
        
        return answer;
    }
}