
class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        ans = 0
        if n < 9:
            return n
        for i in range(1,(n//8)+1):
            ans += 8*i
        return ans + (n % 8)*((n//8)+1)
