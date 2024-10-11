//
// Created by admin on пт.11.10.2024.
//

#include <iostream>
#include <vector>
#include <utility>
#include <unordered_map>
#include <optional>


class Solution {
public:
    static std::pair<int, int> twoSumUnorderedMap(std::vector<int> &nums, int target) {
        std::unordered_map<int, int> numMap;
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            // Убедимся, что дополнение не является самим числом.
            if (numMap.count(complement)) {
                return {numMap[complement], i};
            }
            numMap[nums[i]] = i;
        }
        return {-1, -1};
    };

    // Функция для поиска индексов двух чисел, которые в сумме дают target
    static std::pair<int, int> findTwoSum(const int *nums, size_t size, int target) {
        for (int i = 0; i < size; i++) {
            for (int j = i + 1; j < size; j++) {
                if (nums[i] + nums[j] == target) {
                    return {i, j};  // Возвращаем пару индексов
                }
            }
        }
        return {-1, -1};  // Если пара не найдена
    };

    // Функция для поиска индексов двух чисел, которые в сумме дают target
    static std::vector<int> findTwoSumVector(std::vector<int> &nums, int target) {
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[i] + nums[j] == target) {
                    return {i, j};
                }
            }
        }
        return {};
    };

    // Функция для тестирования
    static void runTest(const std::vector<int> &nums, int target, const std::pair<int, int> &expected) {
        std::pair<int, int> result = findTwoSum(nums.data(), nums.size(), target);

        if (result == expected) {
            std::cout << "Test passed! ";
        } else {
            std::cout << "Test failed! ";
        }

        std::cout << "Input: nums = [";
        for (int i = 0; i < nums.size(); ++i) {
            std::cout << nums[i];
            if (i != nums.size() - 1) std::cout << ", ";
        }
        std::cout << "], target = " << target << "\n";
        std::cout << "Expected: [" << expected.first << ", " << expected.second << "]\n";
        std::cout << "Got: [" << result.first << ", " << result.second << "]\n";
        std::cout << "-----------------------------------\n";
    }
};

int main() {
//    Solution solution;
    // Test case 1
//    Solution::runTest({2, 7, 11, 15}, 9, {0, 1});
//    // Test case 2
//    Solution::runTest({3, 2, 4}, 6, {1, 2});
//    // Test case 3
//    Solution::runTest({3, 3}, 6, {0, 1});

    int target = 26;
    int nums[] = {2, 7, 11, 15};

    std::vector<int> nums_vec(std::begin(nums), std::end(nums));

    std::optional<std::pair<int, int>> resultUnorderedMap = Solution::twoSumUnorderedMap(nums_vec, target);
    std::optional<std::pair<int, int>> resultVector = Solution::findTwoSum(nums, std::size(nums), target);

    if (resultUnorderedMap) {
        std::cout << "Indices for map: " << resultUnorderedMap.value().first << ", "
                  << resultUnorderedMap.value().second << std::endl;
    } else {
        std::cout << "No valid pair found in map." << std::endl;
    }

    if (resultVector) {
        std::cout << "Indices for vector: " << resultVector.value().first << ", " << resultVector.value().second
                  << std::endl;
    } else {
        std::cout << "No valid pair found in vector." << std::endl;
    }

    return 0;
}