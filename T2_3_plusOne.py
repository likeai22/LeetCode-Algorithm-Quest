from typing import List


class Solution:
    @staticmethod
    def plusOne(digits: List[int]) -> List[int]:
        number = int("".join(map(str, digits))) + 1
        new_digits = [int(i) for i in str(number)]
        return new_digits


if __name__ == "__main__":
    print(Solution.plusOne([1, 2, 3]))
