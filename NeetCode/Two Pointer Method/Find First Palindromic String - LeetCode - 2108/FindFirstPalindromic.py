class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for word in words:
            if word == word[::-1]:
                return word
        return ""