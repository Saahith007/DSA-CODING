class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num_sum = 0 
        num_prod = 1
        org = n

        while n > 0:
            num_sum = num_sum + n % 10
            num_prod = num_prod * (n % 10)
            n = n //10

        if org % (num_sum + num_prod) == 0:
            return True
        else:
            return False
        

