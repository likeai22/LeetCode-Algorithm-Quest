//
// Created by admin on пт.11.10.2024.
//

#include <iostream>
#include <string>
#include <algorithm>

int lengthOfLastWordManual(const std::string &s);

int lengthOfLastWord(const std::string &s);


int lengthOfLastWordManual(const std::string &s) {
    if (s.empty()) return 0;

    int arr_len = s.length() - 1;
    int length = 0;

    // Exclude whitespace at the end of the line
    while (arr_len >= 0 && s[arr_len] == ' ') {
        arr_len--;
    }

    // Count the length of the last word
    while (arr_len >= 0 && s[arr_len] != ' ') {
        length++;
        arr_len--;
    }

    return length;
}

int lengthOfLastWord(const std::string &s) {
    // Let s find an iterator for the last non-space
    auto it = std::find_if_not(s.rbegin(), s.rend(), [](char c) { return c == ' '; });

    // Find the length of the last word
    auto word_end = std::find_if(it, s.rend(), [](char c) { return c == ' '; });

    return std::distance(it, word_end);
}

int main() {
    std::string input = " Hello   World  ";

    // Calling a function with manually counting the length of the last word
    int result_manual = lengthOfLastWordManual(input);
    std::cout << "Length of the last word (manual): " << result_manual << std::endl;

    // Calling a function using standard functions
    int result_standard = lengthOfLastWord(input);
    std::cout << "Length of the last word (standard): " << result_standard << std::endl;
}
