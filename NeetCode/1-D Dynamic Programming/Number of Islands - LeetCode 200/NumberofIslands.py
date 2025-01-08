class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        numisland = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    numisland +=1
                    self.dfs(grid,i,j)
        
        return numisland
        
    def dfs(self,grid,i,j):
        if(i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!='1'):
            return
        grid[i][j]=''
        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)
