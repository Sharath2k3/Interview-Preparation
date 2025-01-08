class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count=0
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                a=len(words[i])
                if words[j][:a]==words[i] and words[j][-a:]==words[i]:
                    count+=1
        return count
        