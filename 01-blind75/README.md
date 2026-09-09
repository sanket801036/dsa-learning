# Blind 75

Start this **only after** [`00-prerequisites`](../00-prerequisites) is done.

## Topic split

| Topic | Count |
|---|---|
| Array | 10 |
| Binary | 5 |
| Dynamic Programming | 11 |
| Graph | 8 |
| Interval | 5 |
| Linked List | 6 |
| Matrix | 4 |
| String | 10 |
| Tree | 14 |
| Heap | 3 |

## Rules

- One file per question: `01-two-sum.py`
- Top of the file: problem link, approach in 2 lines, time and space complexity
- Brute force first as a comment, then the optimal solution
- Stuck for 45 minutes? Read the editorial, then re-solve from scratch after 2 days

## File template

```python
"""
Problem : Two Sum
Link    : https://leetcode.com/problems/two-sum/
Topic   : Array, Hashmap

Approach:
    Store each number's index in a dict. For every number, check if
    (target - number) was already seen.

Time  : O(n)
Space : O(n)
"""


def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
```
