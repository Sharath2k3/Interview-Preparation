class Solution(object):
    def canBeValid(self, s, locked):
        if len(s) % 2:  # Intuitively, odd-length s cannot be valid.
            return False

        # traverse each parenthesis forward, treat all unlocked Parentheses as'(' and check if there is ')'
        # that cannot be eliminated by previous '(', if it exists, then the input s can't be valid.
        balance = 0
        for i in range(len(s)):
            #balance += 1 if s[i] == '(' or locked[i] == '0' else -1
            if s[i] == '(' or locked[i]=='0':
                balance+=1
            else:
                balance -=1
            if balance < 0:
                return False

        # traverse each parenthesis backward, treat all unlocked Parentheses as')' and check if there is '('
        # that cannot be eliminated by previous ')', if it exists, then the input s can't be valid.
        balance = 0
        for i in range(len(s) - 1, -1, -1):
            #balance += 1 if s[i] == ')' or locked[i] == '0' else -1
            if s[i] == ')' or locked[i] == '0':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False

        return True