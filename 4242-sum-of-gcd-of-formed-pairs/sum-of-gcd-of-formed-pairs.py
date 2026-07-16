class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0
        prefix_gcd = []
        max_num = 0

        for i in range(n):
            if nums[i] > max_num:
                max_num = max(max_num, nums[i])
            prefix_gcd.append(gcd(nums[i], max_num))
        
        m = len(prefix_gcd)
        prefix_gcd.sort()

        for i in range(m//2):
            total += gcd(prefix_gcd[i],prefix_gcd[m-i-1])
            
        return total