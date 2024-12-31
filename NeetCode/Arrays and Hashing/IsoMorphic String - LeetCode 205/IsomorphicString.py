class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map1 = []
        map2 = []
        for letter in s:
            map1.append(s.index(letter))
        for letter in t:
            map2.append(t.index(letter))
        print(map1,map2)
        if map1==map2:
            return True
        return False