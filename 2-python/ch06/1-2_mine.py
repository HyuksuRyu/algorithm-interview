class Solution:
    def __init__(self):
        pass

    def reverseString(self, s: list[str]) -> None:
        # print(s[::-1])
        s.reverse()
        print(s)


a = Solution()
input_text = ["h", "e", "l", "l", "o"]
a.reverseString(input_text)
input_text = ["H", "a", "n", "n", "a", "h"]
a.reverseString(input_text)

