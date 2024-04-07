class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        ans = [0] * (m + n)
        while True:
            if i == m and j == n:
                break
            elif i == m and j != n:
                ans[i + j:] = nums2[j:n]
                break
            elif i != m and j == n:
                ans[i + j:] = nums1[i:m]
                break
            else:
                num1 = nums1[i]
                num2 = nums2[j]
                if num1 < num2:
                    ans[i + j] = num1
                    i += 1
                elif num1 > num2:
                    ans[i + j] = num2
                    j += 1
                else:
                    ans[i + j] = num1
                    ans[i + j + 1] = num2
                    i += 1
                    j += 1
        nums1[:] = ans[:]
        return nums1
        