class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_dic = {1: 'I', 4:'IV', 5: 'V', 9:'IX', 10: 'X', 40:'XL', 50: 'L', 90: 'XC', 100: 'C', 400:'CD', 500:'D', 900: 'CM', 1000:'M'}
        
        pat = ''
        
        vals = roman_dic.keys()
        vals.sort(reverse = True)
        r = num
        for val in vals:
            x, r = divmod(r, val)
            pat += str(x)
        
        ans = ''
        for idx, val in enumerate(vals):
            for i in range(int(pat[idx])):
                ans += roman_dic[val]
                
        return ans