class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n % 3 == 0:
            return 3**(n/3)
        elif n % 3 == 2:
            return 3**(n/3)*2
        else:
            if n < 3:
                return 1
            if n % 3 == 1:
                return 3**((n/3)-1)*4