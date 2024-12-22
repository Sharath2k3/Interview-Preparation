class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        #If Grid is empty
        if not grid:
            return 0
        
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == '1'):
                    num_islands+=1
                    self.dfs(grid,i,j)

        return num_islands

    def dfs(self,grid,i,j):
        if(i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!='1'):
            return
        grid[i][j] = ''
        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)