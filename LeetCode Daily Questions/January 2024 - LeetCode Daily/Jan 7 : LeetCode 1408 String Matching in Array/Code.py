class Solution(object):
    def stringMatching(self, words):
        arr = ' '.join(words)
        substring = []
        for i in words:
            if arr.count(i)>1:
                substring.append(i)
        return substring