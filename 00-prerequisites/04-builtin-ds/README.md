# 4. Built-in Data Structures (Python)

Do not build these from scratch yet. First learn to *use* them fast.

## Checklist

### list
- [ ] append, pop, insert, remove, index, count, reverse, sort
- [ ] slicing: `a[1:4]`, `a[::-1]`, `a[::2]`
- [ ] 2D list creation: `[[0] * m for _ in range(n)]`
- [ ] Know that `[[0] * m] * n` is a **bug** (all rows share memory)

### dict
- [ ] `d[k]`, `d.get(k, default)`, `d.setdefault`
- [ ] `d.keys()`, `d.values()`, `d.items()`
- [ ] Frequency counting pattern
- [ ] Dict comprehension

### set
- [ ] add, remove, discard
- [ ] Union `|`, intersection `&`, difference `-`
- [ ] Why `x in set` is O(1) but `x in list` is O(n)

### tuple
- [ ] Immutable, so it can be a dict key or go inside a set
- [ ] Useful for storing coordinates: `(row, col)`

### collections
- [ ] `deque` — O(1) `appendleft` and `popleft`, used as a queue in BFS
- [ ] `Counter` — instant frequency map, `.most_common(k)`
- [ ] `defaultdict(list)` and `defaultdict(int)` — no more KeyError

### heapq
- [ ] `heappush`, `heappop`, `heapify`
- [ ] Python heap is a **min heap**
- [ ] Max heap trick: push `-value`
- [ ] `nlargest`, `nsmallest`

### Other useful
- [ ] `sorted(arr, key=lambda x: x[1])` and `reverse=True`
- [ ] `bisect_left`, `bisect_right` (binary search on a sorted list)
- [ ] `math.inf` and `-math.inf` for initial min/max

## The most common pattern in all of DSA

```python
freq = {}
for x in nums:
    freq[x] = freq.get(x, 0) + 1
```

Learn this cold. Half of the array and string questions start here.
