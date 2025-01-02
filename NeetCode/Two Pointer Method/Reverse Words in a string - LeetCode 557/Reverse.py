class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        words = [word[::-1] for word in words]
        words = ' '.join(words)
        return words

        