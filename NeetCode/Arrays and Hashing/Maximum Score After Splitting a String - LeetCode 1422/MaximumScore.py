class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(1,len(s)):
            left = s[0:i]
            left_zero_count = left.count('0')
            right = s[i:len(s)]
            right_one_count = right.count('1')
            res = max(res,left_zero_count+right_one_count)
        return res