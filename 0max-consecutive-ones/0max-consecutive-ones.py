class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        A = nums
        cnt = 0
        ans = 0
        for i in range(N):
            if (i == 0 or A[i] != A[i - 1]) and A[i] == 1:
                cnt = 1
            elif A[i] == 1:
                cnt += 1
            else:
                cnt = 0
            ans = max(ans, cnt)
        return ans