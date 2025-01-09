class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set()
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    visited.add((i,j))
                elif grid[i][j] ==2:
                    queue.append((i,j))
        
        result = 0

        while visited and queue:
            for _ in range(len(queue)):
                i,j = queue.popleft()
                for coords in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                    if coords in visited:
                        visited.remove(coords)
                        queue.append(coords)
            result+=1
        
        return -1 if visited else result 