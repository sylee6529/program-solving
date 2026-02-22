import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        
        Map<String, String> map = Map.of("zero", "0",
                                          "one", "1",
                                          "two", "2",
                                          "three", "3",
                                          "four", "4",
                                          "five", "5",
                                          "six", "6",
                                          "seven", "7",
                                          "eight", "8",
                                          "nine", "9"
                                         );
        
        int i = 0;
        char[] chars = s.toCharArray();
        StringBuilder sb = new StringBuilder("");
        StringBuilder tempS = new StringBuilder("");
        
        while(i < s.length()) {
            System.out.println("ans: " + sb.toString() +  "/ index: " + i);
            char ch = chars[i];
            if(Character.isDigit(ch)) {
                sb.append(ch);
            } else {
                tempS.append(ch);
                String tempStr = tempS.toString();
                System.out.println("@" + tempStr);

                if(map.containsKey(tempStr)) {
                    String val = map.get(tempStr);
                    System.out.println("Add val: " + val);
                    
                    sb.append(val);
                    tempS.setLength(0);
                }
            }
            
            i += 1;
        }
        
        answer = Integer.parseInt(sb.toString());
        
        return answer;
    }
}