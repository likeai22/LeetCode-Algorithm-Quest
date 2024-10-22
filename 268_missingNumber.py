from typing import List


class Solution:
    def radix_sort(self, arr: List[int]) -> List[int]:  # https://thecode.media/radix/
        max_digits = max([len(str(x)) for x in arr])

        base = 10
        bins = [[] for _ in range(base)]
        for i in range(0, max_digits):
            for x in arr:
                digit = (x // base**i) % base
                bins[digit].append(x)
            arr = [x for queue in bins for x in queue]
            bins = [[] for _ in range(base)]
        return arr

    def missingNumber_radix(self, nums: List[int]) -> int:  # beats 95.4
        nums[:] = self.radix_sort(nums)
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)

    @staticmethod
    def missingNumber(nums: List[int]) -> int:  # beats 97.07
        nums = sorted(nums)
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)


if __name__ == "__main__":
    nums = [3, 0, 1]
    digit = Solution.missingNumber(nums)
    print(digit)
