class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        max = -1
        i = len(arr) - 1
        while i>=0:
            temp = arr[i]
            arr[i] = max 
            if temp > max:
                max = temp
            i-=1
        return arr