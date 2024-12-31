class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        
        s_count = {}
        t_count = {}

        for i in range(len(s)):
            t_count[t[i]] = 1+t_count.get(t[i],0)
            s_count[s[i]] = 1+s_count.get(s[i],0)

        return s_count==t_count
        