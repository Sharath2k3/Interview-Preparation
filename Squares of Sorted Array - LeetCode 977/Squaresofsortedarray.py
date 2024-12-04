class Solution:
    def sortedSquares(self, A):
        n = len(A)
        result = [0] * n
        i, j = 0, n - 1
        
        for p in range(n - 1, -1, -1):
            if abs(A[i]) > abs(A[j]):
                result[p] = A[i] ** 2
                i += 1
            else:
                result[p] = A[j] ** 2
                j -= 1
        
        return result
