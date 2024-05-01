class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int max_n = 0;
        int n = 0;
        for(int i = 0; i < nums.length; i++) {
            if(nums[i] == 1) {
                n++;
            } else {
                max_n = Math.max(n, max_n);
                n = 0;
            }
        }
        max_n = Math.max(n, max_n);
        
        return max_n;
    }
}