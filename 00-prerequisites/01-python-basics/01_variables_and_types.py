"""
Topic: Variables, data types, type casting, operators

Run this file:  python 01_variables_and_types.py
Read the comments, change the values, run again. That is how it sticks.
"""


def data_types():
    """Python decides the type on its own. You never write the type."""
    n = 10              # int
    price = 10.5        # float
    name = "sanket"     # str
    is_done = True      # bool

    print(type(n), type(price), type(name), type(is_done))

    # int in Python has NO limit. This matters in DSA.
    # In C++/Java this would overflow. Here it just works.
    big = 2 ** 200
    print("2^200 =", big)


def type_casting():
    """Converting one type to another."""
    s = "42"
    n = int(s)              # str -> int
    print(n + 8)            # 50

    f = 7.9
    print(int(f))           # 7  <- it CUTS the decimal, does not round
    print(round(f))         # 8  <- this rounds

    print(str(99) + "!")    # "99!"
    print(list("abc"))      # ['a', 'b', 'c']

    # Common interview use: turn a number into its digits
    num = 1234
    digits = [int(ch) for ch in str(num)]
    print(digits)           # [1, 2, 3, 4]


def operators():
    a, b = 7, 2

    print(a + b)     # 9
    print(a - b)     # 5
    print(a * b)     # 14
    print(a / b)     # 3.5   <- ALWAYS gives a float
    print(a // b)    # 3     <- floor division, gives an int
    print(a % b)     # 1     <- remainder
    print(a ** b)    # 49    <- power

    # TRAP: floor division rounds DOWN, not toward zero
    print(-7 // 2)   # -4, not -3
    print(-7 % 2)    # 1, not -1   (Python's mod is always non-negative for +ve divisor)

    # Comparison gives a bool
    print(a > b, a == b, a != b)

    # Logical: and / or / not  (not &&, ||, !)
    print(a > 0 and b > 0)
    print(a > 100 or b > 0)
    print(not (a > 100))

    # Chained comparison - very readable, works in Python
    x = 5
    print(0 <= x <= 10)      # True


def swapping():
    """One line swap. You will use this in sorting and two pointers."""
    a, b = 1, 2
    a, b = b, a
    print(a, b)     # 2 1


if __name__ == "__main__":
    print("--- data types ---");   data_types()
    print("\n--- casting ---");    type_casting()
    print("\n--- operators ---");  operators()
    print("\n--- swap ---");       swapping()
