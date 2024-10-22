from typing import List


class Solution:
    @staticmethod
    def missingNumber(nums: List[int]) -> int:
        nums = sorted(nums)
        for i in range(len(nums) + 1):
            if i != nums[i]:
                return i
        return len(nums)


if __name__ == "__main__":
    nums = [3, 0, 1]
    digit = Solution.missingNumber(nums)
    print(digit)
