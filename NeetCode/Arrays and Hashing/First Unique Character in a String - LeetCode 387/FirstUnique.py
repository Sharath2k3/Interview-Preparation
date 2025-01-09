class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_map = {}
        for letter in s:
            hash_map[letter] = 1 + hash_map.get(letter,0)
        for i in range(len(s)):
            if hash_map[s[i]] == 1:
                return i
        return -1