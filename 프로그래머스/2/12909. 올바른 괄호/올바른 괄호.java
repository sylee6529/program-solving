import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        Stack<Character> stack = new Stack<>();
        
        for(char ch : s.toCharArray()) {
            if(ch == '(') {
                stack.push(ch);
            }
            
            else {  // 닫는 괄호가 나왔을 때, 여는 괄호가 아니거나 여는 괄호가 없으면 false
                if(stack.empty() || stack.peek() != '(') {
                    return false;
                }
                else {
                    stack.pop();
                }
            }
        }
        
        // 괄호가 남아있다면, false
        if(!stack.empty()) {
            return false;
        }
        
        return answer;
    }
}