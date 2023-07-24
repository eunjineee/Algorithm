class Solution {
public static String solution(String s) {
        StringBuilder answer = new StringBuilder();
        int index = 0;
        for (char so : s.toCharArray()) {
            if (so == ' ') {
                index = 0;
                answer.append(' ');
            }else{
                // 인덱스가 단어의 홀수 짝수를 결정
                // 인덱스는 0부터, 0은 짝수
                if (index%2 == 0) {
                    answer.append(Character.toUpperCase(so));
                } else {
                    answer.append(Character.toLowerCase(so));
                }
                index += 1;
            }

        }
        return answer.toString();
    }
}