class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left = 1
        right = max(piles)

        while left<right:
            mid = (left+right) / 2

            if self.caneatall(piles,mid,h):
                right = mid
            else:
                left = mid + 1
        
        return left
    
    def caneatall(self,piles,speed,h):
        time = 0
        for pile in piles:
            time = time +( (pile - 1) / speed )+ 1
            if time > h:
                return False
        
        return True