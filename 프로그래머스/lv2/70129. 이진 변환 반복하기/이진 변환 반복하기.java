class Solution {
public static int ZeroDelete(String s){
        int zero_num = 0;
        for (char c: s.toCharArray()){
            if (c == '0'){
                zero_num += 1;
            }
        }
        return zero_num;
    }

    public static int[] solution(String s) {
        int repeat = 0;
        int zero = 0;
        while (!s.equals("1")){
            zero += ZeroDelete(s);
            s = Integer.toString(s.length()-ZeroDelete(s), 2);
            repeat += 1;
        }
        return new int[] {repeat, zero};
    }
}