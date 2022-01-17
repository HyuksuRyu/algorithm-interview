class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]

a = Solution()
input = [2,7, 11, 15]
target = 9
expected = [0, 1]

output = a.twoSum(input, target)
output == expected

                