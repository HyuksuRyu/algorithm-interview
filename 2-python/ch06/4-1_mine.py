import regex as re
import collections
class Solution:
    def __init__(self):
        pass
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = paragraph.lower()
        words = [word for word in re.sub(r'[^\w]', " ", paragraph).split(" ") if word not in banned]
        counts = collections.Counter(words)
        del counts[""]
        return counts.most_common(1)[0][0]


a = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
expected = "ball"
result = a.mostCommonWord(paragraph, banned)
print(result)
print(result == expected)


paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]
expected = "b"

#result = a.mostCommonWord(paragraph, banned)
#print(result)
#print(result == expected)
