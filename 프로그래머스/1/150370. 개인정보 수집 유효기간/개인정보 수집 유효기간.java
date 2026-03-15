import java.util.*;

class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        List<Integer> result = new ArrayList<>();
        
        String[] todayArr = today.split("\\.");
        int todayNum = Integer.parseInt(todayArr[0])*12*28 + Integer.parseInt(todayArr[1]) * 28 + Integer.parseInt(todayArr[2]);
        
        Map<String, Integer> map = new HashMap<>();
        for(String item : terms) {
            String[] sarr = item.split(" ");
            map.put(sarr[0], Integer.parseInt(sarr[1]));
        }
        
        for(int i = 0; i < privacies.length; i++) {
            String p = privacies[i];
            String[] parr = p.split(" ");
            int valM = map.get(parr[1]) * 28;
            
            String[] sDateArr = parr[0].split("\\.");
            int pNum = Integer.parseInt(sDateArr[0])*12*28 + Integer.parseInt(sDateArr[1]) * 28 + Integer.parseInt(sDateArr[2]);
            
            if(todayNum >= pNum + valM) {
                result.add(i+1);               
            }
 
        }
        
        return result.stream().mapToInt(Integer::intValue).toArray();
    }
}