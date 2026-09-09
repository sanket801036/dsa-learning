# 5. Recursion

The single most important prerequisite. Trees, graphs, backtracking and DP are all recursion.

## Checklist

### Understanding
- [ ] What the call stack is, and how a function calls itself
- [ ] Base case and recursive case
- [ ] Draw the recursion tree on paper for `fib(5)`
- [ ] Stack overflow / recursion limit (`sys.setrecursionlimit`)
- [ ] Head recursion vs tail recursion

### Basic problems
- [ ] Print 1 to n, and n to 1
- [ ] Sum of first n numbers
- [ ] Factorial
- [ ] Fibonacci (and see why plain recursion is slow)
- [ ] Power `x^n` in O(log n)
- [ ] Reverse an array using recursion
- [ ] Check palindrome using recursion

### Patterns
- [ ] Parameterised recursion vs functional recursion
- [ ] Generate all subsequences of an array
- [ ] Subsequences whose sum equals k
- [ ] Count subsequences (return an int instead of printing)
- [ ] Print all permutations of a string
- [ ] Merge sort written recursively
- [ ] Quick sort written recursively

### Backtracking intro
- [ ] The choose / explore / un-choose pattern
- [ ] N-Queens
- [ ] Rat in a maze
- [ ] Sudoku solver (just read it once, do not stress)

## Template to memorise

```python
def solve(index, current, result):
    # base case
    if index == len(arr):
        result.append(current[:])
        return

    # choice 1: take
    current.append(arr[index])
    solve(index + 1, current, result)
    current.pop()          # un-choose

    # choice 2: skip
    solve(index + 1, current, result)
```

This take / not-take shape solves a huge number of questions.

## How to debug recursion

Add a print with indentation based on depth. Seeing the tree beats guessing.
