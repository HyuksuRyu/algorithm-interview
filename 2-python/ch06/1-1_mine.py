import regex as re
class Solution:
    def __init__(self):
        pass

    def is_palindrome(self, text: str) -> bool:
        # normalize
        text = text.lower()
        text_norm = re.sub('[^a-z0-9]', '', text)
        return text_norm == text_norm[::-1]
        

a = Solution()
input_text = "race a car"
print(a.is_palindrome(input_text))
input_text = "A man, a plan, a canal: Panama"
print(a.is_palindrome(input_text))

