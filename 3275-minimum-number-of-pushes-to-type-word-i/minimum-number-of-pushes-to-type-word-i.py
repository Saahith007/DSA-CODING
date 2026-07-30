
class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        blocks = n//8
        return (blocks *(blocks+1)*4)+(blocks+1)*(n % 8)
