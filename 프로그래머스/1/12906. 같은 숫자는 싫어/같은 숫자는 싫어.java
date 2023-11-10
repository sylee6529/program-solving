import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer = new int[arr.length];
        int j = 0;
        
        int now = arr[0];
        for(int i = 0; i < arr.length; i++) {
            if(now != arr[i]) {
                answer[j] = now;
                j++;
                now = arr[i];
            }
        }
        answer[j] = now;
        System.out.println(j);
         

        return Arrays.copyOfRange(answer, 0, j+1);
    }
}