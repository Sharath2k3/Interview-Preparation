class Solution(object):
    def minOperations(self, boxes):
        ans = [0]*len(boxes)

        left_count, left_cost =0,0
        right_count, right_cost=0,0 
        n = len(boxes)

        for i in range(1,n):
            if boxes[i-1]=='1':
                left_count +=1
            left_cost += left_count
            ans[i] = left_cost

        for i in range(n-2,-1,-1):
            if boxes[i+1]=='1':
                right_count +=1
            right_cost += right_count
            ans[i]+=right_cost
        
        return ans