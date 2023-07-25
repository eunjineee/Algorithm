class Solution {
    public static int solution(int n) {
        StringBuilder rev_str = new StringBuilder();
        rev_str.append(Integer.toString(n,3));
        rev_str.reverse();
        int answer = Integer.parseInt(rev_str.toString(), 3);
        return answer;
    }
}