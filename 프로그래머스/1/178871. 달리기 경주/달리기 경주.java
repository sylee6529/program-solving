import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        String[] answer = new String[players.length];
        Map<String, Integer> indexMap = new HashMap<>();
        int[] orderArr = new int[players.length];
        
        for(int i=0; i<players.length; i++) {
            indexMap.put(players[i], i);
        }
        
        for(String c : callings) {
            int idx = indexMap.get(c);

            String curPlayer = players[idx];
            String swapPlayer = players[idx-1];
            
            players[idx-1] = curPlayer;
            players[idx] = swapPlayer;
            
            indexMap.put(curPlayer, idx-1);
            indexMap.put(swapPlayer, idx);
        }
        
        
        
        return players;
    }
}