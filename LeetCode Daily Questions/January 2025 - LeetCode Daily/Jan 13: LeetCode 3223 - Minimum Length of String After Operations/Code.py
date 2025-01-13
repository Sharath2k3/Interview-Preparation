class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_map = {}
        for char in s:
            hash_map[char] = 1 + hash_map.get(char,0) 
        delete_count = 0
        for freq in hash_map.values():
            if freq % 2!=0:
                delete_count += freq-1
            else:
                delete_count += freq-2
        
        return len(s) - delete_count
