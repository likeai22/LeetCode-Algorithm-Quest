class Solution:
    @staticmethod
    def my_atoi(s: str) -> int:  # 40 ms runtime beats 42.57%
        int_max = 2**31 - 1
        int_min = -2**31
        number = []
        s = s.strip()

        for i, item in enumerate(s):
            if i == 0 and item in ['-', '+']:
                number.append(item)
            elif item.isdigit():
                number.append(item)
            else:
                break

        if not number or (len(number) == 1 and number[0] in ['-', '+']):
            return 0

        result = int("".join(number))

        if result > int_max:
            return int_max
        elif result < int_min:
            return int_min
        else:
            return result

    @staticmethod
    def my_atoi_opt(s: str) -> int:  # 30 ms runtime beats 93.51%
        int_max = 2**31 - 1
        int_min = -2**31
        s = s.strip()

        if not s:
            return 0

        sign = -1 if s[0] == '-' else 1
        if s[0] in ['-', '+']:
            s = s[1:]

        number = 0
        for char in s:
            if not char.isdigit():
                break
            number = number * 10 + int(char)

        number *= sign

        if number > int_max:
            return int_max
        elif number < int_min:
            return int_min
        else:
            return number
