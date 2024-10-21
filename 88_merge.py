from typing import List


class Solution:
    @staticmethod
    def merge(
        nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:  # Wrong Answer
        """
        Do not return anything, modify nums1 in-place instead.
        """
        new_array = []
        nums1 = nums1[:m]
        nums2 = nums2[:n]
        while min(len(nums1), len(nums2)) > 0:
            if nums1[0] > nums2[0]:
                to_insert = nums2.pop(0)
                new_array.append(to_insert)
            elif nums1[0] <= nums2[0]:
                to_insert = nums1.pop(0)
                new_array.append(to_insert)
        if len(nums1) > 0:
            for i in nums2:
                new_array.append(i)
        if len(nums2) > 0:
            for i in nums2:
                new_array.append(i)
        nums1[:] = new_array[:]


class Solution:
    @staticmethod
    def merge(
        nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:  # O((m+n)log(m+n))
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m]

        i, j, k = 0, 0, 0

        while i < m:
            nums1[k] = nums1_copy[i]
            i += 1
            k += 1
        while j < n:
            nums1[k] = nums2[j]
            j += 1
            k += 1

        nums1[:] = sorted(nums1)


class Solution:
    @staticmethod
    def merge(
        nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:  # O((m+n)log(m+n))
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2[:n])


class Solution:
    @staticmethod
    def merge(
            nums1: List[int], m: int, nums2: List[int], n: int
    ) -> None:  # O((m+n)log(m+n))
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m]
        nums1_copy.extend(nums2[:n])
        nums1[:] = sorted(nums1_copy)


class Solution:
    @staticmethod
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:  # O(m+n)
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m]

        i, j, k = 0, 0, 0

        while i < m and j < n:
            if nums1_copy[i] <= nums2[j]:
                nums1[k] = nums1_copy[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1

        while i < m:
            nums1[k] = nums1_copy[i]
            i += 1
            k += 1

        while j < n:
            nums1[k] = nums2[j]
            j += 1
            k += 1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    Solution.merge(nums1, 3, [2, 5, 6], 3)
    print(nums1)
