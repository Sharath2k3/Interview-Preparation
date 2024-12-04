class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        prevrows = self.generate(numRows-1)
        prevrow = prevrows[-1]
        currentrow = [1]

        for i in range(1,numRows-1):
            currentrow.append(prevrow[i-1]+prevrow[i])

        currentrow.append(1)
        prevrows.append(currentrow)

        return prevrows 