import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public static ArrayList getAnswer(int yellow){
        ArrayList answer = new ArrayList<>();
        for (int i = (int) Math.sqrt(yellow); i > 0; i--){
            if (yellow % i == 0){
                answer.add(new int[] {i, yellow/i});
            }
        }
        return answer;
    }

    public static int[] solution(int brown, int yellow){
        ArrayList answer = getAnswer(yellow);
        List<Integer> total = new ArrayList<>();
        for (Object obj : answer){
            // 이 과정이 왜 있어야하는지 모르겠음
            int[] arr = (int[]) obj;
            ///////////
            int a = arr[0];
            int b = arr[1];
            if ((a+b)*2+4 == brown){
                total.add(b+2);
                total.add(a+2);
            }
        }
        return total.stream().mapToInt(i -> i).toArray();
    }
}