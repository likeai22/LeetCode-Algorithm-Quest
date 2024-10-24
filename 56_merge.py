import sys
from typing import List


class Solution:
    @staticmethod
    def merge_old(intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 0
        while i < len(intervals) - 1:
            if (
                intervals[i][0] <= intervals[i + 1][0]
                and intervals[i][1] >= intervals[i + 1][1]
            ):
                del intervals[i + 1]
                continue
            if intervals[i][1] >= intervals[i + 1][0]:
                intervals[i][1] = intervals[i + 1][1]
                del intervals[i + 1]
                continue
            i += 1
        return intervals

    def insert_sort_guarded(self, intervals: List[List[int]]) -> List[List[int]]:  # 5.08 95.35
        """
        Сортировка вставками со сторожевым элементом (переписал С++ код сортировки на Python)
        """
        backup = intervals[0]
        intervals[0] = [-(sys.maxsize + 1)]

        for i in range(1, len(intervals)):
            x = intervals[i]
            j = i - 1

            while intervals[j] > x:
                intervals[j + 1] = intervals[j]
                j -= 1

            intervals[j + 1] = x

        j = 1
        while j < len(intervals) and intervals[j] < backup:
            intervals[j - 1] = intervals[j]
            j += 1

        intervals[j - 1] = backup

        return intervals

    def radix_sort(self, arr: List[List[int]], key_idx: int = 0) -> List[List[int]]:  # 92.55 78.86
        max_digits = max([len(str(num)) for sublist in arr for num in sublist])
        base = 10
        bins = [[] for _ in range(base)]
        for i in range(0, max_digits):
            for x in arr:
                digit = (x[key_idx] // base**i) % base
                bins[digit].append(x)
            arr = [x for queue in bins for x in queue]
            # for bin_list in bins:
            #     bin_list.clear()  # << 92.34
            bins = [[] for _ in range(base)]
        return arr

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # intervals.sort(key=lambda x: x[0])  # 94.52
        intervals = self.radix_sort(intervals)
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            if merged[-1][1] >= intervals[i][0]:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                merged.append(intervals[i])

        return merged


if __name__ == "__main__":
    intervals = [[1, 4], [0, 2], [3, 5]]
    intervals = Solution().merge(intervals)
    print(intervals)
