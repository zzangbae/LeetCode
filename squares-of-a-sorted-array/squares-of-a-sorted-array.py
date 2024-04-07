class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        
        for num in nums:
            ans.append(num**2)
        
        ans.sort()
        
        return ans