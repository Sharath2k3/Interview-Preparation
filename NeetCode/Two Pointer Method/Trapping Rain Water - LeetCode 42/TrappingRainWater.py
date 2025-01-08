class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height)-1
        lmax = 0
        rmax = 0
        ans = 0
        while l<r:
            lmax = max(lmax,height[l])
            rmax = max(rmax,height[r])
            if lmax<rmax:
                ans = ans + (lmax - height[l])
                l+=1
            else:       
                ans = ans + (rmax - height[r])
                r-=1
        return ans
     