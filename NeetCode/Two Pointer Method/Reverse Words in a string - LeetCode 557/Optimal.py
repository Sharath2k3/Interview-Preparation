class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.strip().split()
        res = []
        for word in words:
            i=0
            j=len(word)-1
            while(i<j):
                word = list(word)
                word[i],word[j]=word[j],word[i]
                i+=1
                j-=1
            temp = (''.join(word))
            res.append(temp)
        return ' '.join(res)