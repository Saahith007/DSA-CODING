class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = Counter(s)
        left = ""
        mid = ""
        
        for ch in sorted(freq):
            left+=(ch*(freq[ch]//2))

            if freq[ch] % 2:
                mid = ch
        
        
        return left+mid+left[::-1]
