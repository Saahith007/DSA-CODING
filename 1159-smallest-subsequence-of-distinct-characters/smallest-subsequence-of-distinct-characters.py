class Solution:
    def smallestSubsequence(self, s: str) -> str:
        n = len(s)
        m = len(set(s))

        seen = set()
        stack = []
        last_str = {char: i for i, char in enumerate(s)}

        for i,char in enumerate(s):
            if char in seen:
                continue

            while stack and stack[-1] > char and last_str[stack[-1]] > i:
                seen.remove(stack.pop())

            stack.append(char)
            seen.add(char)
        return "".join(stack)

