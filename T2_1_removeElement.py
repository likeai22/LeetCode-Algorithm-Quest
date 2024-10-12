from typing import List


class Solution:
    @staticmethod
    def remove_element(nums: List[int], val: int) -> int:  # 34 ms runtime beats 76.44%
        for item in range(len(nums) - 1, -1, -1):
            if nums[item] == val:
                del nums[item]
        return len(nums)

    @staticmethod
    def remove_element_opt(nums: List[int], val: int) -> int:  # 31 ms runtime beats 90.5%
        while val in nums:
            nums.remove(val)
        return len(nums)
