class Solution:
    @staticmethod
    def license_key_formatting(s: str, k: int) -> str:
        # Удаляем дефисы и преобразуем в верхний регистр
        s = s.replace("-", "").upper()

        # Определяем количество символов в первой группе
        first_group_len = len(s) % k

        # Если длина первой группы равна нулю, то первая группа равна k
        if first_group_len == 0:
            first_group_len = k

        # Формируем первую группу
        result = s[:first_group_len]

        # Добавляем остальные группы
        for i in range(first_group_len, len(s), k):
            result += "-" + s[i: i + k]

        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.license_key_formatting("5F3Z-2e-9-w", 4))
    print(solution.license_key_formatting("2-5g-3-J", 2))
