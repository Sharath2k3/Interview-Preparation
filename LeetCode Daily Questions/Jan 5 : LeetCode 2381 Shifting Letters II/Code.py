class Solution:
    def shiftingLetters(self, s, shifts):
        n = len(s)
        prefix_sum = [0] * (n+1)

        for start,end,direction in shifts:
            if direction == 1:
                value = 1
            else:
                value = -1
            prefix_sum[start] += value
            prefix_sum[end+1] -= value
        
        for i in range(1,n):
            prefix_sum[i]+=prefix_sum[i-1]

        result = list(s)
        for i in range(n):
            total_shift = prefix_sum[i]
            total_shift = ((total_shift%26)+26)%26

            new_char = (ord(s[i])-ord('a')+total_shift)%26
            result[i] = chr(ord('a')+new_char)

        return ''.join(result)
