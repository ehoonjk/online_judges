# 104ms
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_li = list(s)
        t_li = list(t)
        s_li.sort()
        t_li.sort()
        
        if s_li == t_li:
            return True
        else:
            return False