class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] arr = new int[m + n];
        
        int aidx = 0;
        int bidx = 0;
        for(int i = 0; i < m + n; i++) {
            // need finish condition
            if(aidx == m) {
                arr[i] = nums2[bidx];
                bidx++;
                continue;
            }
            if(bidx == n) {
                arr[i] = nums1[aidx];
                aidx++;
                continue;
            }
            if(nums1[aidx] < nums2[bidx]) {
                arr[i] = nums1[aidx];
                aidx++;
            } else {
                arr[i] = nums2[bidx];
                bidx++;
            }
        }
        for(int i = 0; i < m + n; i++) {
            nums1[i] = arr[i];
        }
    }
}