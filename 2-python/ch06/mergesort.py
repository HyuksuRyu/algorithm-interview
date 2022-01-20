class MergeSort:
    def __init__(self):
        pass
    def merge_sort(self, L: list) -> list:
        if len(L) == 2:
            if L[0] <= L[1]:
                return [L[0], L[1]]
            else:
                return [L[1], L[0]]

        else:
            middle = len(L) // 2
            left = self.merge_sort(L[:middle])
            right = self.merge_sort(L[middle:])
            return self.merge(left, right)

    def merge(self, left: list, right: list) -> list:
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1
        
        while j < len(right):
            result.append(right[j])
            j += 1
        return result

a = MergeSort()
inp = [23, 3, 45, 7, 6, 11, 14, 12]
result = a.merge_sort(inp)
print(result)