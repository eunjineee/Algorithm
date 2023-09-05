class Solution {
   public static int solution(int n) {
        long[] num = new long[n+2];
        num[0] = 0;
        num[1] = 1;

        for (int i = 0; i < n; i++){
           num[i+1] = (num[i+1] + num[i]) % 1234567;
           if (i+2 < num.length) num[i+2] += num[i];
        }

        int ans = (int) (num[n] % 1234567);
        return ans;
    }
}