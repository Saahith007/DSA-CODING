class Solution:
    def maxProduct(self, n: int) -> int:
        arr = []
        digit = 0 

        while n >0:
            digit = n % 10
            n = n // 10
            arr.append(digit)
        
        arr.sort(reverse = 'True')
        return arr[0]*arr[1]