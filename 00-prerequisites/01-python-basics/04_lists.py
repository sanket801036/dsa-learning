"""
Topic: Lists - the array of Python

90% of DSA questions hand you a list. Know every operation and its cost.
"""


def operations():
    a = [3, 1, 4, 1, 5]

    print(len(a))           # 5
    print(a[0], a[-1])      # 3 5   <- negative index counts from the end

    a.append(9)             # O(1)   add at the end
    a.insert(0, 0)          # O(n)   add at the front - SLOW, shifts everything
    print(a)

    a.pop()                 # O(1)   remove last
    a.pop(0)                # O(n)   remove first - SLOW
    print(a)

    a.remove(1)             # O(n)   removes the FIRST 1, not all of them
    print(a)

    print(a.index(4))       # O(n)   position of value 4
    print(a.count(1))       # O(n)   how many 1s

    a.sort()                # O(n log n)  in place
    print(a)
    a.reverse()             # O(n)   in place
    print(a)

    b = sorted(a)           # returns a NEW sorted list, 'a' untouched
    print(b)


def slicing():
    a = [0, 1, 2, 3, 4, 5]

    print(a[1:4])       # [1, 2, 3]     stop is EXCLUDED
    print(a[:3])        # [0, 1, 2]
    print(a[3:])        # [3, 4, 5]
    print(a[::2])       # [0, 2, 4]     every 2nd
    print(a[::-1])      # [5, 4, 3, 2, 1, 0]   reversed
    print(a[:])         # full copy

    # Slicing makes a NEW list -> costs O(k) time and O(k) space.
    # Inside a loop this can quietly turn O(n) into O(n^2). Be careful.


def comprehension():
    nums = [1, 2, 3, 4, 5, 6]

    squares = [x * x for x in nums]
    print(squares)

    evens = [x for x in nums if x % 2 == 0]
    print(evens)

    labels = ["even" if x % 2 == 0 else "odd" for x in nums]
    print(labels)

    # Flatten a 2D list
    grid = [[1, 2], [3, 4], [5, 6]]
    flat = [x for row in grid for x in row]
    print(flat)


def two_d_lists():
    n, m = 3, 4

    # CORRECT way to make a 3x4 grid of zeros
    grid = [[0] * m for _ in range(n)]
    grid[0][0] = 1
    print(grid)         # only row 0 changed - correct

    # WRONG way - all rows are the SAME list object
    bad = [[0] * m] * n
    bad[0][0] = 1
    print(bad)          # every row changed! classic bug

    # Traversing a grid
    for i in range(n):
        for j in range(m):
            print(grid[i][j], end=" ")
        print()


def useful_builtins():
    a = [3, 1, 4, 1, 5]

    print(sum(a), min(a), max(a))
    print(any(x > 4 for x in a))     # True if at least one matches
    print(all(x > 0 for x in a))     # True if every one matches

    # Sort by a custom key - you will use this a LOT
    pairs = [(1, 'b'), (3, 'a'), (2, 'c')]
    print(sorted(pairs, key=lambda p: p[1]))            # by letter
    print(sorted(pairs, key=lambda p: p[0], reverse=True))  # by number, desc

    # zip - walk two lists together
    for x, y in zip([1, 2, 3], ['a', 'b', 'c']):
        print(x, y, end="  ")
    print()


if __name__ == "__main__":
    print("--- operations ---");   operations()
    print("\n--- slicing ---");    slicing()
    print("\n--- comprehension ---"); comprehension()
    print("\n--- 2D ---");         two_d_lists()
    print("\n--- builtins ---");   useful_builtins()
