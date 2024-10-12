from typing import List


class Solution:
    @staticmethod
    def remove_duplicates(nums: List[int]) -> int:  # 3106 ms runtime beats 5.04%
        for item in nums:
            while nums.count(item) > 1:
                nums.remove(item)
        return len(nums)

    @staticmethod
    def remove_duplicates_opt(nums: List[int]) -> int:  # 75 ms runtime beats 59.03%
        if not nums:
            return 0

        left = 0

        for right in range(1, len(nums)):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]

        return left + 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    print(sol.remove_duplicates_opt([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
