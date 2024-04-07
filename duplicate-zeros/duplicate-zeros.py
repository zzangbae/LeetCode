class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        l = len(arr)
        idx = 0             # ans's index
        while idx < l:
            if arr[idx] == 0:
                arr.insert(idx, 0)
                arr.pop()
                idx += 2
            else:
                idx += 1
        
        return arr