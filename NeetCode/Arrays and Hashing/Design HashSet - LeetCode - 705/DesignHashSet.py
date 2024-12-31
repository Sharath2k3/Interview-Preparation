class MyHashSet(object):

    def __init__(self):
        self.set = {}

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.set[key] = 1
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.set[key] = 0

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        x = self.set.get(key,0)
        if x==0:
            return False
        else:
            return True


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)