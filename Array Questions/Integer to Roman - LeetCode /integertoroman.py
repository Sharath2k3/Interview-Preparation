class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = []
        data = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),(100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),(9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        for digit,symbol in data:
            if num==0:
                break
            count_of_each_symbol = num // digit
            res.append(count_of_each_symbol * symbol)
            num = num - count_of_each_symbol * digit
        return ''.join(res)