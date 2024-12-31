class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = set()
        for email in emails:
            local,domain = email.split('@')
            temp = ""
            for c in local:
                if c=='.':
                    continue
                elif c=='+':
                    break
                else:
                    temp += c
            res.add(temp+"@"+domain)
        return len(res)