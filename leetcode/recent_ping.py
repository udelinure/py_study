class RecentCounter(object):

    def __init__(self):
        self.listoftime = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.listoftime.append(t)
        while self.listoftime[0] < t - 3000:
            self.listoftime.pop(0)
        return len(self.listoftime)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
