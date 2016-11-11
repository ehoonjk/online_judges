# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        v = n 
        temp = 1
        while temp < v:
            mid = (v + temp) / 2
            if isBadVersion(mid):
                v = mid
            else:
                temp = mid + 1
        return v