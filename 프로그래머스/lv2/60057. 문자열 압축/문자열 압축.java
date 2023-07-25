class Solution {
public static int solution(String s) {
        int answer = s.length();
        for (int i = 1; i <= s.length(); i++) {
            int num = i * 2;                       // 다음 범위 마지막 숫자
            int total = s.length();              // 원래 s 문자열 길이
            String word = s.substring(0, i);      // 첫번째 비교할 문자열
            int repeat = 0;                      // 반목한 숫자

            while (num <= s.length()) {
                if (word.equals(s.substring(num - i, num))) {
                    repeat += 1;
                } else {
                    word = s.substring(num - i, num);
                    if (repeat != 0) {
                        total -= (repeat * i - Integer.toString(repeat + 1).length());
                        repeat = 0;
                    }
                }
                num += i;
            }
            if (repeat != 0) {
                total -= (repeat * i - Integer.toString(repeat + 1).length());
                repeat = 0;
            }
            if (answer > total) {
                answer = total;
            }
        }
        return answer;
    }
}