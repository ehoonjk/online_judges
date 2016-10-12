class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        ans = 0
        s = str(num)
        if len(s) == 1:
            return num
        else:
            for val in s:
                ans += int(val)
            ans = self.addDigits(ans)
            return ans
        