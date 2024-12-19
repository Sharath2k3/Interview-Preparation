class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return True
        string = ""
        for x in s:
            if x != " " and x.isalpha() or x.isnumeric():
                string+=x
        string = string.lower()
        left=0
        right = len(string)-1
        while(left<right):
            if(string[left]!=string[right]):
                return False
            left+=1
            right-=1
        return True