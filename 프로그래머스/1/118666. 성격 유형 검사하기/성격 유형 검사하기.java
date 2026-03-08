import java.io.*;
import java.util.*;

class Solution {
    public String solution(String[] survey, int[] choices) {
        String answer = "";
        Map<String, Integer> map = new HashMap<>(Map.of(
            "R", 0,
            "T", 0,
            "C", 0,
            "F", 0,
            "J", 0,
            "M", 0,
            "A", 0,
            "N", 0
        ));
        
        for(int i=0; i<choices.length; i++) {
            int score = Math.abs(choices[i] - 4);
            if(choices[i] < 4) {
                String leftType = survey[i].charAt(0) + "";
                map.put(leftType, map.getOrDefault(leftType, 0) + score);
            } else if(choices[i] > 4) {
                String rightType = survey[i].charAt(1) + "";
                map.put(rightType, map.getOrDefault(rightType, 0) + score);
            } 
        }
        
        System.out.println(map);
        
        if(map.get("R") >= map.get("T")) {
            answer += "R";
        } else {
            answer += "T";
        }
        
        if(map.get("C") >= map.get("F")) {
            answer += "C";
        } else {
            answer += "F";
        }
        
        if(map.get("J") >= map.get("M")) {
            answer += "J";
        } else {
            answer += "M";
        }
        
        if(map.get("A") >= map.get("N")) {
            answer += "A";
        } else {
            answer += "N";
        }
        
        return answer;
    }
    
}