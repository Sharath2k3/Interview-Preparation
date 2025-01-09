class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter+=4
                    if grid[i-1][j] ==1 and i>0:
                        perimeter -=2
                    if grid[i][j-1]== 1 and j>0:
                        perimeter -=2
        return perimeter