from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        res = 0
        majority = 0

        for n in nums:
            hash[n] = 1 + hash.get(n,0)
            if hash[n]>majority:
                res = n
                majority = hash[n]

        return res