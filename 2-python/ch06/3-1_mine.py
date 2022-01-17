class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        # split log -> digit, letter
        digits = []
        letters = []

        for log in logs:
            if log.split(" ")[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # sort letters lexicographically
        letters.sort(key=lambda x: (x.split(" ")[1:], x.split(" ")[0]))

        return letters + digits

a = Solution()
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
expected = ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
result = a.reorderLogFiles(logs)
print(result)
print(result == expected)

logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
expected = ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
result = a.reorderLogFiles(logs)
print(result)
print(result == expected)

letters.sort(key=lambda x: (x.split(" ")[1:], x.split(" ")[0]))