class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen = set()
        for i in arr:
            if 2*i in seen and i/2 in seen:
                print(2*i,i/2)
                return True
            seen.add(i)
        return False
        