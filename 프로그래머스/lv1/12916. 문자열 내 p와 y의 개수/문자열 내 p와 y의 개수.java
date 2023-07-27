class Solution {
    public static boolean solution(String s){
        int answer = 0;
        for (char c: s.toCharArray()) {
            if (c == 'p' || c == 'P') {
                answer += 1;
            } else if (c == 'y' || c == 'Y') {
                answer -= 1;
            }
        }
        return answer==0 ? true : false;
    }
}