class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        max_freq = [0] * 26
        for word in words2:
            freq = [0] * 26
            for char in word:
                freq[ord(char)-ord('a')] +=1
            
            for i in range(26):
                max_freq[i]= max(max_freq[i],freq[i])
        
        res = []
        for word in words1:
            word_freq = [0] * 26
            for char in word:
                word_freq[ord(char)-ord('a')]+=1
            
            is_universal = True
            for i in range(26):
                if word_freq[i] < max_freq[i]:
                    is_universal = False
                    break
            
            if is_universal:
                res.append(word)
        
        return res