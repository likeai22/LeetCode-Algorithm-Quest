from functools import lru_cache


class Solution:
    def fib_easy(self, n: int) -> int:  # 34.35% 24.22%
        if n == 0 or n == 1:
            return n
        return self.fib_easy(n - 1) + self.fib_easy(n - 2)

    @lru_cache(maxsize=32)
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


if __name__ == "__main__":
    res = Solution().fib(4)
    print(res)
