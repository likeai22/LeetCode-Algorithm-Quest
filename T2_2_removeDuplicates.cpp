//
// Created by admin on сб.12.10.2024.
//

#include <iostream>
#include <algorithm>
#include <vector>


class Solution {
public:
    static int removeDuplicates(std::vector<int> &nums) {
        if (nums.size() <= 1) {
            return nums.size();
        }

        int i = 0;

        for (int j = 1; j < nums.size(); j++) {
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
            }
        }

        return i + 1;
    }
};

int main() { // 4 ms runtime beats 84.85%
    int nums[] = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};

    std::vector<int> nums_vec(std::begin(nums), std::end(nums));

    int result = Solution::removeDuplicates(nums_vec);
    std::cout << "Length of the array: " << result << std::endl;

    return 0;
}