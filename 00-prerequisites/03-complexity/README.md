# 3. Time and Space Complexity

Every interview ends with "what is the complexity?". Learn it early, not later.

## Checklist

- [ ] What time complexity actually measures (operations, not seconds)
- [ ] What space complexity measures (extra memory, not input)
- [ ] Big-O, Big-Theta, Big-Omega — what each one means
- [ ] Drop constants and lower terms: `O(3n + 5)` becomes `O(n)`
- [ ] Complexity of a single loop, two loops in sequence, nested loops
- [ ] Loop where `i` doubles each time -> `O(log n)`
- [ ] Recursion complexity using a recursion tree
- [ ] Master theorem (just the basic form)
- [ ] Amortised complexity (why `list.append` is O(1))
- [ ] Complexity of common Python operations

## The ladder (fastest to slowest)

```
O(1) < O(log n) < O(sqrt(n)) < O(n) < O(n log n) < O(n^2) < O(n^3) < O(2^n) < O(n!)
```

## Rough guide from constraints

If a question says `n <= ...`, the expected complexity is usually:

| n | Expected |
|---|---|
| 10^18 | O(log n) or O(1) |
| 10^8 | O(n) |
| 10^6 | O(n) or O(n log n) |
| 10^5 | O(n log n) |
| 10^4 | O(n^2) |
| 500 | O(n^3) |
| 20 to 25 | O(2^n) |
| 10 to 11 | O(n!) |

Read the constraints first. They tell you the answer's shape before you start.

## Python operation costs

| Operation | Complexity |
|---|---|
| `list[i]`, `list.append(x)` | O(1) |
| `list.insert(0, x)`, `list.pop(0)` | O(n) |
| `x in list` | O(n) |
| `x in set` / `x in dict` | O(1) average |
| `dict[k] = v` | O(1) average |
| `list.sort()` | O(n log n) |
| `heapq.heappush` / `heappop` | O(log n) |
| string `+=` in a loop | O(n^2) — use a list and `join` |
