class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        map = {}
        map['b'] = 0
        map['a'] = 0
        map['l'] = 0
        map['o'] = 0
        map['n'] = 0

        for txt in text:
            if txt in map:
                map[txt]+=1
        
        #print(map)
        return min(map['b'],map['a'],map['l']//2,map['o']//2,map['n'])