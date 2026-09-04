class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        n = len(nums)
        curr_min = float('inf')

        for i in range(n):
            max_idx = max(nums[:i+1])
            min_idx = min(nums[i:n])
            in_idx = max_idx - min_idx
            curr_min = min(curr_min,in_idx)
            
            if curr_min <=k:
                return i
                break
        return -1
