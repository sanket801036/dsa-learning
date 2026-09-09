"""
Topic: Input and output

LeetCode gives you a function - no input reading needed.
Codeforces / CodeChef / GFG give you stdin - you MUST read it yourself.
Know both.

This file does not run interactively by default. Read it, then try the
examples by uncommenting and piping input:
    echo "5" | python 06_input_output.py
"""

import sys


def normal_input_examples():
    """
    input() always returns a STRING. Cast it yourself.

    # single number
    n = int(input())

    # single line of numbers: "1 2 3 4"
    arr = list(map(int, input().split()))

    # two numbers on one line: "3 5"
    a, b = map(int, input().split())

    # n lines, one number each
    n = int(input())
    arr = [int(input()) for _ in range(n)]

    # a grid of n rows
    grid = [list(input().strip()) for _ in range(n)]
    """
    pass


def fast_input_examples():
    """
    input() is slow when n is large (10^5 or more). Use sys.stdin.

    input = sys.stdin.readline          # then use input() as normal
    n = int(input())
    arr = list(map(int, input().split()))

    # Read EVERYTHING at once - fastest option
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:n+1]))

    Note: sys.stdin.readline keeps the trailing newline.
    Use .strip() when reading strings, not needed for int().
    """
    pass


def output_examples():
    print("hello")
    print(1, 2, 3)                  # hello 1 2 3 -> space separated
    print(1, 2, sep=",")            # 1,2
    print("no newline", end="")     # does not move to next line
    print()

    arr = [1, 2, 3]
    print(*arr)                     # 1 2 3    <- unpacks the list
    print(" ".join(map(str, arr)))  # same thing, works for any list

    # f-strings - the clean way to format
    name, score = "sanket", 95.5
    print(f"{name} scored {score}")
    print(f"{score:.1f}")           # 1 decimal place

    # Printing inside a big loop is SLOW. Collect and print once:
    out = []
    for i in range(3):
        out.append(str(i))
    print("\n".join(out))


def demo_reading_stdin():
    """Actually runs if you pipe something in."""
    data = sys.stdin.read().split()
    if not data:
        print("(no stdin given - pipe something in to see this work)")
        return
    nums = list(map(int, data))
    print("read:", nums)
    print("sum :", sum(nums))


if __name__ == "__main__":
    print("--- output ---")
    output_examples()
    print("\n--- stdin ---")
    demo_reading_stdin()
