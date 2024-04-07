class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        
        for num in nums:
            cnt = 0
            while num > 0:
                num /= 10
                cnt += 1
            if cnt % 2 == 0:
                ans += 1
                
        return ans
        