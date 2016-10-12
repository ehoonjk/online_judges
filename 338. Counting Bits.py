class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = []
        for i in range(0, num+1):
            count = self.count_bit("{0:b}".format(i))
            ans.append(count)
        return ans
    
    def count_bit(self, val):
        count = 0
        for i in val:
            if 1 == int(i):
                count += 1
        return count