import java.util.HashMap;
import java.util.Map;
class Solution {
    public static Integer solution(String before, String after){
        for (char b : before.toCharArray()){
            if (after.contains(String.valueOf(b))) {
                String bb = String.valueOf(b);
                after = after.replaceFirst(bb," ");
            } else {
                return 0;
            }
        }
        for (char a : after.toCharArray()){
            if (a != ' '){
                return 0;
            }
        }
        return 1;
    }
}