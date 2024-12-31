class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split(' ')
        if len(pattern) != len(words):
            return False

        pattern_map,word_map = {},{}
        for i in range(len(pattern)):
            if pattern_map.get(pattern[i],-1) != word_map.get(words[i],-1):
                return False
            pattern_map[pattern[i]] = i
            word_map[words[i]] = i 
        
        return True
        