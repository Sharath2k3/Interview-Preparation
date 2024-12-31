class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_map = {}
        for i in range(len(nums)):
            num_map[nums[i]] = 1 + num_map.get(nums[i],0)

        sorted_elements = sorted(num_map.items(), key=lambda x: x[1], reverse=True)

        return [element for element, _ in sorted_elements[:k]]