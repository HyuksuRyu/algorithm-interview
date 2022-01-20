class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Detect Palindrom and expand two pointers
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                text_sample = s[left+1:right]
            return s[left + 1:right]

        # simple check
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        # make sliding window go right
        for i in range(len(s) -1):
            text_a = expand(i, i+1)
            text_b = expand(i, i+2)
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)

        return result


a = Solution()
text = "ac"
print(a.longestPalindrome(text))