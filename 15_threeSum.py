from typing import List


class Solution:
    @staticmethod
    def threeSum_old(nums: List[int]) -> List[List[int]]:
        result = []
        unique_triplets = set()
        nums.sort()

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            if len(set(nums)) > 1 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                if left == i:
                    left += 1
                elif right == i:
                    right -= 1
                summ = nums[left] + nums[right]
                if summ + nums[i] == 0:
                    key = tuple([nums[i], nums[left], nums[right]])
                    if key not in unique_triplets:
                        unique_triplets.add(key)
                        result.append(list(key))
                if summ + nums[i] > 0:
                    right -= 1
                else:
                    left += 1
            left += 1
            right -= 1
        return result

    @staticmethod
    def threeSum(nums: List[int]) -> List[List[int]]:
        result = []
        unique_triplets = set()
        nums.sort()

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            if i > 1 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                summ = nums[i] + nums[left] + nums[right]
                if summ == 0:
                    key = (nums[i], nums[left], nums[right])
                    if key not in unique_triplets:
                        unique_triplets.add(key)
                        result.append(list(key))
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif summ < 0:
                    left += 1
                else:
                    right -= 1

        return result


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]  # Accepted
    result = Solution.threeSum(nums)
    print("result", result)
