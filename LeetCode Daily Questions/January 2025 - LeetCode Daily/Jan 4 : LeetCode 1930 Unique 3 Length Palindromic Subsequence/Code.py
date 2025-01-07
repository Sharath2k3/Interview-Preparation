from collections import defaultdict

class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_map = defaultdict(list)
        
        # Store the indices of each character in the string
        for i in range(len(s)):
            hash_map[s[i]].append(i)
        print(hash_map)
        res = 0
        
        # Loop through each character in the hash_map
        for element in hash_map:
            if len(hash_map[element]) < 2:
                continue
                
            # First and last occurrence of the current character
            a = hash_map[element][0]
            b = hash_map[element][-1]
            
            # Count distinct characters in the middle part of the string
            # This is to form palindromes of length 3 like "aba", "aca", etc.
            #print(s[a+1:b])
            res += len(set(s[a+1:b]))
        
        return res

# Example usage
solution = Solution()
input_str = "aabca"
output = solution.countPalindromicSubsequence(input_str)
print(output)  # Expected Output: 3
