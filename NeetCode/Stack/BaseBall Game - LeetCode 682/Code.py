class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        for operation in operations:
            if operation == 'C':
                stack.pop()
            elif operation == 'D':
                stack.append(stack[-1]*2)
            elif operation == '+':
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(operation))
        return sum(stack)
        