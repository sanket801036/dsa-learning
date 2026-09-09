# 6. Basic Algorithms and Patterns

Once these are done, you are ready for the 75 questions.

## Checklist

### Sorting (write each one yourself once)
- [ ] Bubble sort — O(n^2)
- [ ] Selection sort — O(n^2)
- [ ] Insertion sort — O(n^2), but fast on nearly sorted data
- [ ] Merge sort — O(n log n), stable, O(n) extra space
- [ ] Quick sort — O(n log n) average, O(n^2) worst
- [ ] When to just use `sorted()` (almost always in an interview, after you explain the rest)

### Searching
- [ ] Linear search
- [ ] Binary search on a sorted array
- [ ] First and last occurrence of a target
- [ ] Lower bound and upper bound
- [ ] Binary search on the **answer** (this one is a big pattern)

### Two pointers
- [ ] Pair with a given sum in a sorted array
- [ ] Remove duplicates in place
- [ ] Move zeroes to the end
- [ ] Container with most water

### Sliding window
- [ ] Fixed size window: max sum of k consecutive elements
- [ ] Variable size window: longest substring without repeating characters
- [ ] Know when to shrink the window

### Prefix sum
- [ ] Build a prefix sum array
- [ ] Range sum query in O(1)
- [ ] Subarray sum equals k (prefix sum + hashmap)

### Kadane
- [ ] Maximum subarray sum

## Pattern cheat sheet

| If the question says | Try |
|---|---|
| sorted array, find a pair | two pointers |
| contiguous subarray / substring | sliding window |
| range sums, many queries | prefix sum |
| sorted array, find one element | binary search |
| "minimum largest" or "maximum smallest" | binary search on the answer |
| top k / k largest | heap |
| count occurrences, seen before? | dict or set |
| all combinations, all paths | recursion + backtracking |
