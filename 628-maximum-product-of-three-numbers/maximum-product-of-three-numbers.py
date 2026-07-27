class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        prod1 = nums[-3]*nums[-2]*nums[-1]
        prod2 = nums[0]*nums[1]*nums[-1]
        return prod1 if prod1 > prod2 else prod2