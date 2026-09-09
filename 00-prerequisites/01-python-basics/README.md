# 1. Python Basics

Goal: never get stuck on syntax during a problem.

## Checklist

- [ ] Variables and data types (int, float, str, bool)
- [ ] Type casting: `int()`, `str()`, `float()`, `list()`
- [ ] Operators: arithmetic, comparison, logical, `//`, `%`, `**`
- [ ] Conditionals: `if` / `elif` / `else`
- [ ] Loops: `for`, `while`, `range()`, `break`, `continue`
- [ ] Nested loops and how to trace them on paper
- [ ] Functions: arguments, default values, `return`, multiple returns
- [ ] Mutable vs immutable (why a list changes inside a function but an int does not)
- [ ] Lists: index, slice, append, pop, insert, remove, len
- [ ] List comprehension: `[x*x for x in nums if x > 0]`
- [ ] Strings: immutability, slicing, `split`, `join`, `strip`, `replace`, `find`
- [ ] f-strings for printing
- [ ] Tuples and unpacking: `a, b = b, a`
- [ ] `enumerate()` and `zip()`
- [ ] Input handling: `input()`, `map(int, input().split())`
- [ ] Fast input for big cases: `sys.stdin.readline`

## Practice ideas

- Reverse a list without using `[::-1]`
- Find the max and min in a list with one loop
- Count vowels in a string
- Print a right-angle star pattern, then a pyramid
- Check if a string is a palindrome

## Gotchas

- `list2 = list1` does **not** copy. Use `list1.copy()` or `list1[:]`.
- Default mutable argument bug: `def f(x, arr=[])` keeps the same list across calls.
- Integer division `7 // 2` is `3`, but `-7 // 2` is `-4`, not `-3`.
