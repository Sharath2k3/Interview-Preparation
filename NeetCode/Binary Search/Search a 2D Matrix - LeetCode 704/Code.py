class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or target is None:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows*cols -1

        while left <= right:
            mid = (left+right) /2 
            mid_value = matrix[mid/cols][mid%cols]

            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
