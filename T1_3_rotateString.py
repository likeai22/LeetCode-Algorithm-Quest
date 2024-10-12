class Solution:
    @staticmethod
    def rotate_string(s: str, goal: str) -> bool:
        if len(goal) != len(s) or set(goal) != set(s):
            return False
        for i in range(len(s)):
            new_word = s[i+1:] + s[:i+1]
            if new_word == goal:
                return True
        return False


if __name__ == "__main__":
    solution = Solution()
    solution.rotate_string("abcde", "cdeab")
    solution.rotate_string("abcde", "abced")

