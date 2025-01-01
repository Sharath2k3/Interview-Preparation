class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        pos = [0, 0]  # Start position
        visited = set()  # Set to store visited positions
        visited.add(tuple(pos))  # Add the starting position to the set
        
        for direction in path:
            # Update the position based on the direction
            if direction == 'N':
                pos[1] += 1
            elif direction == 'E':
                pos[0] += 1
            elif direction == 'W':
                pos[0] -= 1
            elif direction == 'S':
                pos[1] -= 1
            
            # Check if the current position has been visited before
            if tuple(pos) in visited:
                return True  # Path crosses itself
            
            # Add the current position to the visited set
            visited.add(tuple(pos))
        
        return False  # No crossing detected
