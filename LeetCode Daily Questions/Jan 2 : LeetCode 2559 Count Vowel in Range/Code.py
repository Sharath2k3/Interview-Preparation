class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(words)
        pre = [0] * (n + 1)  # Prefix array to store cumulative counts
        vowels = set('aeiou')  # Set of vowels for quick lookup

        # Compute prefix sum where pre[i+1] holds count of words that start and end with a vowel
        for i in range(n):
            pre[i + 1] = pre[i]
            if words[i][0] in vowels and words[i][-1] in vowels:
                pre[i + 1] += 1
        print(pre)
        # Answer each query by calculating the difference between indices in the prefix array
        #x=[pre[r + 1] - pre[l] for l, r in queries]
        #print(x)
        return [pre[r + 1] - pre[l] for l, r in queries]
        #return [pre[r + 1] - pre[l] for l, r in queries]


# Example Test Case
words = ["aba", "bcb", "ece", "aa", "e"]
queries = [[0, 2], [1, 4], [1, 1]]

# Instantiate the Solution class and call the function
sol = Solution()
result = sol.vowelStrings(words, queries)
print(result)  # Output: [2, 3, 0]
