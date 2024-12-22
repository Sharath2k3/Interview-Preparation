class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for ele in nums:
            if ele in seen:
                return True
            else:
                seen.add(ele)
        return False