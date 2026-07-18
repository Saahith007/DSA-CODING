class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minimum = float('inf')
        maximum = float('-inf')

        for i in range(len(nums)):
            if nums[i] > maximum:
                maximum = nums[i]
            if nums[i] < minimum:
                minimum = nums[i]
            
        return gcd(maximum,minimum)