class Solution {
    public int removeElement(int[] nums, int val) {
        int ans = 0;
        int[] arr;
        for(int num : nums) {
            if(num != val)
                ans++;
        }
        arr = new int[ans];
        int idx = 0;    // arr's index
        for(int num : nums) {
            if(num != val) {
                arr[idx] = num;
                idx++;
            }
        }
        for(int i = 0; i < ans; i++)
            nums[i] = arr[i];
        for(int i = ans; i < nums.length; i++)
            nums[i] = 0;
        return ans;
    }
}