import java.util.HashSet;
import java.util.Set;
class Solution {
    public static int solution(int[] numbers) {
        int answer = 45;
        Set<Integer> arr = new HashSet<>();
        for (int i : numbers){
            arr.add(i);
        }

        for (int j : arr){
            answer -= j;
        }

        return answer;
    }
}