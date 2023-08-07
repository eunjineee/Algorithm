import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    static char[] sol1 = {1,2,3,4,5}; //5
    static char[] sol2 = {2,1,2,3,2,4,2,5}; //8
    static char[] sol3 = {3,3,1,1,2,2,4,4,5,5}; // 10


    public static int[] solution(int[] answer){
        int ans1 = 0;
        int ans2 = 0;
        int ans3 = 0;

        for (int i = 0; i < answer.length; i++){
            int s1 = 0;
            int s2 = 0;
            int s3 = 0;

            if (i != 0) {
                s1 = i % 5;
                s2 = i % 8;
                s3 = i % 10;
            }

            if (answer[i] == sol1[s1]) ans1 += 1;
            if (answer[i] == sol2[s2]) ans2 += 1;
            if (answer[i] == sol3[s3]) ans3 += 1;
        }

        int[] total = {ans1, ans2, ans3};
        List<Integer> answer_li = new ArrayList<>();
        int max_num = 0;
        for (int j: total){
            if (j >= max_num){
                max_num = j;
            }
        }

        for (int j =0; j < 3; j++){
            if (total[j] == max_num){
                answer_li.add(j+1);
            }
        }
        return answer_li.stream().mapToInt(i -> i).toArray();
    }
}