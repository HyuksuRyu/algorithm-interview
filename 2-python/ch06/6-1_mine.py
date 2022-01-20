class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # is number of letters even? odd?
        def _is_even_string(s: str) -> bool:
            if len(s) % 2 == 0:
                return True
            else:
                return False
        
        
        if not _is_even_string(s):
            cent_i = int((len(s) - 1)/2)
        
            palindrom_string = s[cent_i]
            # 중앙에서부터 한 글자씩 늘려가면서 Palidrome 확인
            # 5글자: [2]에서 시작하여 [2] 포함 [1:3]&[2:4] / [0:3]&[2:5] 비교
            # 7글자: [3]에서 시작하여 [3] 포함 [2:4]&[3:5] / [1:4]&[3:6] / [0:4]&[3:7] 비교
            for i in range(1, cent_i+1):
                if s[cent_i-i:cent_i+1] == s[cent_i:cent_i+1+i][::-1]:
                    palindrom_string = s[cent_i-1:cent_i+1+i]
        
        else:
            # string has even number
            # the string has two centrics, which are [len(s)/2 - 1] & [len(s)/2]
            # 2 letters: cent_i = [0,1] -> [0] & [1]
            # 4 letters: cent_i = [1,2] -> [1] & [2], [0:2] & [2:4]
            # 6 letters: cent_i = [2,3] -> [2] & [3], [1:3] & [3:5], [0:3] & [3:6]
            # 8 letters: cent_i = [3,4] -> [3] & [4], [2:4] & [4:6], [1:4] & [4:7], [0:4] & [4:8]
            
            cent_i = int(len(s)/2) # cent_i-1, cent_i
            palindrom_string = s[cent_i]
            
            if s[cent_i - 1] == s[cent_i]:
                palindrom_string = s[cent_i-1:cent_i+1]
            
            for i in range(1, cent_i):
                if s[cent_i-i:cent_i] == s[cent_i:cent_i+i][::-1]:
                    palindrom_string = s[cent_i-i:cent_i+i]
                    
        return palindrom_string
                