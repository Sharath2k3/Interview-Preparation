class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        left = right = 0

        while left < len(s) and right < len(t):
            if s[left] == t[right]:
                left += 1
            right += 1
        
        return left == len(s)