class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        numset = set(nums)
        for i in range(1,len(nums)+1):
            if i not in numset:
                res.append(i)
        return res