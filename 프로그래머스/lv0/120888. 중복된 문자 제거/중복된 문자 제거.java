import java.util.HashSet;
import java.util.Set;
class Solution {
    public static String solution(String my_string){
        Set<Character> strings = new HashSet<>();
        String new_string = "";
        for (char c : my_string.toCharArray()){
            if (!strings.contains(c)){
                strings.add(c);
                new_string += c;
            }
        }
        return new_string;
    }
}