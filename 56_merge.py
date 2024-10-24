from typing import List


class Solution:
    @staticmethod
    def merge(intervals: List[List[int]]) -> List[List[int]]:
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


if __name__ == "__main__":
    intervals = [[1, 4], [0, 2], [3, 5]]
    Solution.merge(intervals)
    print(intervals)
