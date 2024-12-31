class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        fin = []
        for rowindex in range(numRows):
            res =  [1]
            prev = 1
            for k in range(1,rowindex+1):
                next_val = prev * (rowindex-k+1) // k #Pascal Triangle's Formula
                res.append(next_val)
                prev=next_val
            fin.append(res)
        return fin
