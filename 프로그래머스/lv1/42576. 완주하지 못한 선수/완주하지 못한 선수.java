import java.util.HashMap;
import java.util.Map;
class Solution {
    public static String solution(String[] participant, String[] completion) {
        Map<String, Integer> count = new HashMap<>();

        for (String s: participant){
            count.putIfAbsent(s, 0);
            count.put(s, count.get(s)+1);
        }

        for (String c: completion){
            int v = count.get(c) -1;
            count.put(c,v);
            if (v==0) count.remove(c);
        }
        // HashMap의 마지막 원소를 가져오는 방법
        return count.keySet().iterator().next();
    }
}