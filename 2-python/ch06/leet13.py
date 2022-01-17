class Solution:
    def romanToInt(self, s:str) -> int:
        roman_dict = {'I': 1,
                      'V': 5,
                      'X': 10,
                      'L': 50,
                      'C': 100,
                      'D': 500,
                      'M': 1000 }
        roman_sub_dict = {'IV': 4,
                         'IX': 9,
                         'XL': 40,
                         'XC': 90,
                          'CD': 400,
                          'CM': 900
                         }
        sum = 0
        for i, char in enumerate(s):
            if i == 0:
                if s[i:i+2] in roman_sub_dict:
                    continue
                else:
                    sum += roman_dict[char]
            else:
                if s[i-1:i+1] in roman_sub_dict:
                    sum += roman_sub_dict[s[i-1:i+1]]
                elif s[i:i+2] in roman_sub_dict:
                    continue
                else:
                    sum += roman_dict[char]
        return sum

a = Solution()
input = "MCDLXXVI"
expected = 1476
output = a.romanToInt(input)
print(output)