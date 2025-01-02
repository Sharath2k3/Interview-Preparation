class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        i1,i2,j1,j2=0,0,0,0
        while i1<len(word1) and i2<len(word2):
            if word1[i1][j1] != word2[i2][j2]:
                return False

            #Move the Characters in both arrays
            j1+=1
            j2+=1

            if j1==len(word1[i1]):
                i1+=1
                j1=0
            
            if j2==len(word2[i2]):
                i2+=1
                j2=0

            if i1 == len(word1) and i2 == len(word2):
                return True

        return False