class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first_largest = second_largest = 0
        first_smallest = second_smallest = float("inf")

        for n in nums:
            if n < first_smallest:
                second_smallest,first_smallest = first_smallest,n
            elif n < second_smallest:
                second_smallest = n
            
            if n>first_largest:
                second_largest,first_largest = first_largest,n
            elif n>second_largest:
                second_largest = n
            
        return first_largest * second_largest - first_smallest * second_smallest