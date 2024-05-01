class Solution {
    public int findNumbers(int[] nums) {
        // 자리수가 짝수인
        // String으로
        int n = 0;
        for(int i = 0; i < nums.length; i++) {
            String s = Integer.toString(nums[i]);
            if(s.length() % 2 == 0)
                n++;
        }
        return n;
    }
}