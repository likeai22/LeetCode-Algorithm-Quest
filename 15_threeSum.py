from typing import List


class Solution:
    @staticmethod
    def threeSum0(nums: List[int]) -> List[List[int]]:
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
                    key = tuple(sorted([nums[i], nums[left], nums[right]]))
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


if __name__ == "__main__":
    # nums = [-1, 0, 1, 2, -1, -4]  # Accepted
    # nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]
    # nums = [0, 0, 0]
    nums =[34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]
    result = Solution.threeSum(nums)
    print("result", result)
