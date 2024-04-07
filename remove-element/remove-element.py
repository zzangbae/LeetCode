class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ans = []
        cnt = 0     # zero count
        for num in nums:
            if num == val:
                cnt += 1
                continue
            else:
                ans.append(num)
        nums[:] = ans[:]