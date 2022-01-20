from typing import List
class Solution:
    def reorder_log(self, logs:List[str]) -> List[str]: 
        texts = []
        digits = []

        for log in logs:
            if log.split(' ')[1].isdigit():
                digits.append(log)
            else:
                texts.append(log)

        texts.sort(key=lambda x: (x.split(' ')[1], x.split(' ')[0]))

        return texts + digits
