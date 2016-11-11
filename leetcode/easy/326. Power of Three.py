class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n>0:
            return (math.log10(n) / math.log10(3)) % 1 == 0
        
        else:
            return False
            
            