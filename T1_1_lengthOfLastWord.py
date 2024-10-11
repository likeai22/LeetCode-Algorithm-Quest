# 58. Length of Last Word
class Solution:
    @staticmethod
    def length_of_last_word(s: str) -> int:
        words = s.strip().split()
        if not words:
            return 0
        return len(words[-1])

    @staticmethod
    def length_of_last_word_manual(s: str) -> int:
        arr_len = len(s) - 1
        length = 0

        # Exclude whitespace at the end of the line
        while arr_len >= 0 and s[arr_len] == " ":
            arr_len -= 1

        # Count the length of the last word
        while arr_len >= 0 and s[arr_len] != " ":
            length += 1
            arr_len -= 1
        return length


if __name__ == "__main__":
    s = " Hello   World  "
    sol = Solution()

    print(sol.length_of_last_word(s))
    print(sol.length_of_last_word_manual(s))
