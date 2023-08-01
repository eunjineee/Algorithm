class Solution {
    public static String solution(String s){
        s = s.toLowerCase();
        s = s.replaceAll("[^a-z0-9\\-_.]","");
        s = s.replaceAll("\\.+",".");
        s = s.replaceAll("^\\.","");
        s = s.replaceAll("\\.$","");
        if (s.length() == 0){
            s = "a";
        } else if (s.length() >= 16) {
            s = s.substring(0,15);
            s = s.replaceAll("\\.$", "");
        }
        while (s.length() < 3){
            s += s.substring(s.length()-1,s.length());
        }
        return s;
    }
}