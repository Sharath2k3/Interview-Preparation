class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        current_score = s[:1].count("0") + s[1:].count("1")
        max_score = current_score
        for i in range(1, len(s)-1):
            if s[i] == "0":
                current_score = current_score + 1
            else:
                current_score = current_score - 1
            if current_score > max_score:
                max_score = current_score
        
        return max_score