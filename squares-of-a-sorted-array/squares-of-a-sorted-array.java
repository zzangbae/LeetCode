class Solution {
    public int[] sortedSquares(int[] nums) {
        int l = nums.length;
        int[] numSq = new int[l];
        for(int i = 0; i < l; i++) {
            numSq[i] = (int)Math.pow(nums[i], 2);
        }
        Arrays.sort(numSq);
        return numSq;
    }
}