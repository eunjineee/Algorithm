import java.util.*;


class Solution {
        public static int[] solution(String[] gems){
        int N = gems.length;
        int[] answer = new int[]{0, N-1};
        int kind = new HashSet<>(Arrays.asList(gems)).size();
        Map<String, Integer> dic = new HashMap<>();
        dic.put(gems[0], 1);
        int s=0, e=0;

        while (s < N && e < N) {
            if (dic.size() < kind) {
                e++;
                if (e == N) {
                    break;
                }
                dic.put(gems[e], dic.getOrDefault(gems[e], 0) + 1);
            } else {
                if (e - s + 1 < answer[1] - answer[0] + 1) {
                    answer[0] = s;
                    answer[1] = e;
                }
                if (dic.get(gems[s]) == 1) {
                    dic.remove(gems[s]);
                } else {
                    dic.put(gems[s], dic.get(gems[s]) - 1);
                }
                s++;
            }
        }
        answer[0]++;
        answer[1]++;
        return answer;
    }
}