class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        numbers = '123456789'
        res = []
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)+1):
                temp = int(numbers[i:j])
                if low<=temp<=high:
                    res.append(temp)
        res.sort()
        return res