class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        for num in nums:
            if num == 0:
                count += 1
                
        for i in range(count):
            nums.remove(0)
            nums.append(0)
            

            