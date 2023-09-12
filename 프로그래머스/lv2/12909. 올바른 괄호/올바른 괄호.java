import java.util.Stack;

class Solution {
    public static boolean solution(String s) {
        Stack<Integer> stack = new Stack<>();

        for (char c : s.toCharArray()){
            if (c == '('){
                stack.add(0);
            }else{
                if (stack.isEmpty()){
                    return false;
                }else{
                    stack.pop();
                }
            }
        }
        return stack.isEmpty();
    }
}