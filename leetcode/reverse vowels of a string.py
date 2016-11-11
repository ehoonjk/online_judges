class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aeiouAEIOU'
        vowel_list = []
        for chr in s:
            if chr in vowels:
                vowel_list.append(chr)
        
        ans = ''
        
        for chr in s:
            if chr in vowels:
                ans += vowel_list.pop()
            else:
                ans += chr
                
        return ans