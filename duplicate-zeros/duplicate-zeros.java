class Solution {
    public void duplicateZeros(int[] arr) {
        int zeroCnt = 0;
        for(int i = 0; i < arr.length; i++)
            if(arr[i] == 0)
                zeroCnt++;
        int[] ans = new int[arr.length + zeroCnt];
        int idx = 0;    // ans index
        
        for(int i = 0; i < arr.length; i++) {
            if(arr[i] != 0) {
                ans[idx] = arr[i];
                idx++;
            } else {
                ans[idx] = 0;
                ans[idx + 1] = 0;
                idx += 2;
            }
        }
        for(int i = 0; i < arr.length; i++)
            arr[i] = ans[i];
    }
}