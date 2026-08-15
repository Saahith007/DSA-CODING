class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        cur_xor = 0
       

        for num in nums:
            cur_xor = cur_xor ^ num

        if nums.count(0) == n:
            return 0

        if cur_xor!=0:
            return n
        
        elif cur_xor == 0:
            return n-1
        else:
            return 0
            

        



        

        