class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        res = []
        i = 0
        for space in spaces:
            res.append(s[i:space])
            res.append(' ')
            i = space
        res.append(s[i:])
        return ''.join(res)