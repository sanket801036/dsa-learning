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

## Files in this folder

Run each one and read the comments. They are written to be read, not just executed.

| File | Covers |
|---|---|
| `01_variables_and_types.py` | data types, casting, operators, swap |
| `02_conditionals_and_loops.py` | if/elif, for, while, nested loops, patterns |
| `03_functions.py` | arguments, return, mutable vs immutable, copy trap |
| `04_lists.py` | list ops and their cost, slicing, comprehension, 2D grids |
| `05_strings.py` | immutability, methods, ord/chr, common problems |
| `06_input_output.py` | input(), fast stdin, formatted output |
| `07_practice.py` | 13 problems with built-in tests |

```bash
python 01_variables_and_types.py
python 07_practice.py            # should print 13 PASS lines
```

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
