# 84ms
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_li = [0]*26
        t_li = [0]*26
        if len(s) != len(t):
            return False
            
        for idx in range(len(s)):
            i = ord(s[idx])-97
            j = ord(t[idx])-97
            s_li[i] += 1
            t_li[j] += 1
            
        if s_li == t_li:
            return True
        else:
            return False

        