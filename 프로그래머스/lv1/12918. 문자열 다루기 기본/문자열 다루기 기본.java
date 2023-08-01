class Solution {
    public static Boolean solution(String s){
        boolean answer = false;
        if (s.length() == 4 || s.length() == 6){
            answer = s.matches("[0-9]*");
            Boolean answer2 = s.matches("[0-9]*");
            System.out.println(answer2);
        }
        return answer;
    }
}