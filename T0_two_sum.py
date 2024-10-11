from typing import List


class Solution:
    def __init__(self, nums: List[int], target: int):
        self.target = target
        self.nums = nums
        if not (2 <= len(self.nums) <= 10000) or not (-(10**9) <= self.target <= 10**9):
            raise ValueError("2 <= nums.length <= 10^4, -10^9 <= target <= 10^9")
        for i, item in enumerate(self.nums):
            if not (-(10**9) <= item <= 10**9):
                raise ValueError(
                    f"Element nums[{i}] = {item} is out of allowed range -10^9 <= nums[i] <= 10^9"
                )

    def twoSum(self) -> List[int]:  # brute force
        for i, first_num in enumerate(self.nums):
            for j, second_num in enumerate(self.nums[i + 1 :]):
                if first_num + second_num == self.target:
                    return [i, j + i + 1]

    def twoSum2(self) -> List[int]:
        seen = {}
        for i, num in enumerate(self.nums):
            complement = self.target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


if __name__ == "__main__":
    sol_1 = Solution(nums=[2, 7, 11, 15], target=26)
    sol_2 = Solution(nums=[3, 2, 4], target=6)
    sol_3 = Solution(nums=[3, 3], target=6)

    print(sol_1.twoSum())
    print(sol_1.twoSum2())

    print(sol_2.twoSum())
    print(sol_2.twoSum2())

    print(sol_3.twoSum())
    print(sol_3.twoSum2())
