class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.strip().split(' ')
        length_of_last_word = len(words[-1])
        return length_of_last_word