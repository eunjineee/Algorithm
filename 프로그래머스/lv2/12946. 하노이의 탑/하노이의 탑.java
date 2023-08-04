import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    private static  List<int[]> hanoi(int n, int from, int to){
        if (n == 1){
            return Arrays.asList(new int[]{from, to});
        }

        int empty = 6 - from - to;

        List<int[]> result = new ArrayList<>();
        result.addAll(hanoi(n-1, from, empty));
        result.addAll(hanoi(1, from, to));
        result.addAll(hanoi(n-1, empty, to));
        return result;
    }

    public static int[][] solution(int i){
        return hanoi(i,1, 3).toArray(new int[0][]);
    }
}