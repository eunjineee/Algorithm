import java.util.Stack;

class Solution {
    public static boolean ifAnswer(char[] str){
        Stack<Character> stack = new Stack<>();

        for (char c: str){
            switch (c){
                case '[' -> stack.add(']');
                case '{' -> stack.add('}');
                case '(' -> stack.add(')');
                case ']', '}', ')' -> {
                    if (stack.isEmpty()) return false;
                    if (stack.pop() != c) return false;
                }
            }
        }
        return stack.isEmpty();
    }

    public static char[] CharToBack(char[] chars){
        if (chars.length <= 1) {
            return chars;
        }

        char firstChar = chars[0];

        for (int i = 0; i < chars.length - 1; i++) {
            chars[i] = chars[i + 1];
        }

        chars[chars.length - 1] = firstChar;
        return chars;
    }

    public static int solution(String s) {
        char[] str = s.toCharArray();
        int answer = 0;
        for (int i=0; i < s.length(); i++){
            if (ifAnswer(str)){
                answer += 1;
            }
            str = CharToBack(str);
        }

        return answer;
    }
}