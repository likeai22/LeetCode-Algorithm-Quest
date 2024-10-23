from typing import List


class Solution:
    @staticmethod
    def arrayPairSum0(nums: List[int]) -> int:
        nums.sort()
        max_sum = 0
        for i in range(len(nums) // 2):
            for j in range(len(nums)):
                max_sum += min(nums[i * 2 + j], nums[i * 2 + j + 1])
                break
        return max_sum

    @staticmethod
    def arrayPairSum(nums: List[int]) -> int:
        nums.sort()
        max_sum = 0
        for i in range(0, len(nums), 2):
            max_sum += min(nums[i], nums[i + 1])
        return max_sum


if __name__ == "__main__":
    nums = [6, 2, 6, 5, 1, 2]
    summ = Solution.arrayPairSum(nums)
    print(summ)
