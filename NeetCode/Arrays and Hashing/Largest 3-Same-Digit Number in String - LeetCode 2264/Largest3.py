class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        result = -1
        for i in range(len(num)-2):
            if num[i]==num[i+1] and num[i+1] == num[i+2]:
                result = max(result,int(num[i]))
        return "" if result == -1 else str(result)*3
