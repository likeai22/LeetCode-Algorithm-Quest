from typing import List


class Solution:
    @staticmethod
    def threeSum(nums: List[int]) -> List[List[int]]:
        result = []
        unique_triplets = set()
        nums.sort()

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            if len(nums) > 3 and nums[i] == nums[i - 1]:
                break
            while left < right:
                if left == i:
                    left += 1
                elif right == i:
                    right -= 1
                summ = nums[left] + nums[right]
                if summ + nums[i] == 0:
                    key = tuple(sorted([nums[i], nums[left], nums[right]]))
                    if not key in unique_triplets:
                        unique_triplets.add(key)
                        result.append(list(key))
                if summ + nums[i] > 0:
                    right -= 1
                else:
                    left += 1
            left += 1
            right -= 1
        return result


if __name__ == "__main__":
    # nums = [-1, 0, 1, 2, -1, -4]  # Accepted
    # nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    nums = [0, 0, 0]
    result = Solution.threeSum(nums)
    print("result", result)
