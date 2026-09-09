"""
Topic: if / elif / else, for, while, nested loops

Nested loops are the reason most brute force solutions are O(n^2).
Learn to TRACE them on paper - that is how you find the complexity.
"""


def conditionals():
    n = 0

    if n > 0:
        print("positive")
    elif n < 0:
        print("negative")
    else:
        print("zero")

    # Short form (ternary). Handy inside a loop.
    label = "even" if n % 2 == 0 else "odd"
    print(label)

    # Python has no switch. Use a dict instead.
    grade = {90: "A", 80: "B", 70: "C"}
    print(grade.get(80, "not found"))


def for_loops():
    # range(stop)
    for i in range(5):
        print(i, end=" ")       # 0 1 2 3 4
    print()

    # range(start, stop)
    for i in range(2, 6):
        print(i, end=" ")       # 2 3 4 5
    print()

    # range(start, stop, step)
    for i in range(0, 10, 2):
        print(i, end=" ")       # 0 2 4 6 8
    print()

    # Backwards - VERY common in DSA (traversing an array from the end)
    for i in range(5, 0, -1):
        print(i, end=" ")       # 5 4 3 2 1
    print()

    # Loop over a list directly when you do not need the index
    nums = [10, 20, 30]
    for x in nums:
        print(x, end=" ")
    print()

    # Need both index and value? Use enumerate.
    for i, x in enumerate(nums):
        print(f"index {i} -> {x}")


def while_loops():
    # Use while when you do not know the number of steps in advance
    n = 1234
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    print("digits:", count)     # 4

    # break and continue
    for i in range(10):
        if i == 3:
            continue            # skip this one
        if i == 6:
            break               # stop the whole loop
        print(i, end=" ")
    print()


def nested_loops():
    """
    Outer loop runs n times, inner loop runs n times.
    Total = n * n  ->  O(n^2)
    """
    n = 3
    for i in range(n):
        for j in range(n):
            print(f"({i},{j})", end=" ")
        print()

    # Star patterns train your loop sense. Do these on paper first.
    print("\nright triangle:")
    for i in range(1, 5):
        print("*" * i)

    print("\npyramid:")
    n = 4
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)


if __name__ == "__main__":
    print("--- conditionals ---");  conditionals()
    print("\n--- for ---");         for_loops()
    print("\n--- while ---");       while_loops()
    print("\n--- nested ---");      nested_loops()
