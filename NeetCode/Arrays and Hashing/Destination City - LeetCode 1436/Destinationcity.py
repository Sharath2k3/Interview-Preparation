    class Solution(object):
        def destCity(self, paths):
            """
            :type paths: List[List[str]]
            :rtype: str
            """
            depaturecities = set(path[0] for path in paths)
            for path in paths:
                if path[1] not in depaturecities:
                    return path[1]
        