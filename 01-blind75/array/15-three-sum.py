"""
Problem : 3Sum
Link    : https://leetcode.com/problems/3sum/
Topic   : Array, Two Pointers, Sorting
Prereq  : ../../00-prerequisites/06-basic-algorithms/01_two_pointers.py

Given nums, return ALL unique triplets [a, b, c] where a + b + c == 0.
"Unique" is the hard part. The sum is easy.

Time  : O(n^2)     - one outer loop x one linear two-pointer scan
Space : O(1)       - not counting the output list (sort is in place)
"""


# ------------------------------------------------ approach 1: brute force

def three_sum_brute(nums):
    """
    Three nested loops, then de-duplicate with a set.
    Time  O(n^3)
    Space O(k) for the set

    n = 3000 on LeetCode, so n^3 = 27 billion -> TLE.
    But write it first. It shows you understand the problem.
    """
    n = len(nums)
    found = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    # sort the triplet so [-1,0,1] and [0,1,-1] look the same
                    found.add(tuple(sorted([nums[i], nums[j], nums[k]])))
    return [list(t) for t in found]


# --------------------------------------------- approach 2: sort + 2 pointers

def three_sum(nums):
    """
    THE IDEA
        Fix one number. Now you need two more that sum to -(that number).
        That is exactly 2Sum on a sorted array -> two pointers.

        So: sort once, then for each i run a two-pointer scan on the rest.

        outer loop  O(n)
        inner scan  O(n)
        ------------------
        total       O(n^2)

    Sorting costs O(n log n), which is smaller than O(n^2), so it is free.
    Sorting also gives us duplicate handling almost for granted, because
    equal values end up next to each other.
    """
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 2):

        # Optimisation: array is sorted, so if the smallest of the three
        # is already positive, every sum from here on is > 0. Stop.
        if nums[i] > 0:
            break

        # DUPLICATE GUARD 1 (for the fixed number)
        # If this value is the same as the previous one, we already found
        # every triplet starting with it. Skip.
        #   [-1, -1, 0, 1, 2]
        #     i=0 handles both -1 cases, so skip i=1
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1
        target = -nums[i]

        while left < right:
            total = nums[left] + nums[right]

            if total < target:
                left += 1               # need bigger
            elif total > target:
                right -= 1              # need smaller
            else:
                result.append([nums[i], nums[left], nums[right]])

                # move BOTH - we are done with this pair
                left += 1
                right -= 1

                # DUPLICATE GUARD 2 (for the pair)
                # Skip over repeats so we do not record the same triplet.
                #   [-2, 0, 0, 2, 2]  with i=0: (0,2) is valid, but the
                #   second 0 and second 2 would give (0,2) all over again.
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return result


# --------------------------------------------------------------- tests

def normalise(triplets):
    """Sort so we can compare regardless of order."""
    return sorted(sorted(t) for t in triplets)


def check(name, got, want):
    g, w = normalise(got), normalise(want)
    print(f"[{'PASS' if g == w else 'FAIL'}] {name:<22} got={g!r}")
    if g != w:
        print(f"         expected={w!r}")


if __name__ == "__main__":
    # the standard example
    check("basic", three_sum([-1, 0, 1, 2, -1, -4]),
          [[-1, -1, 2], [-1, 0, 1]])

    # no triplet exists
    check("none", three_sum([0, 1, 1]), [])

    # all zeros - must return ONE triplet, not many
    check("all zeros", three_sum([0, 0, 0]), [[0, 0, 0]])
    check("four zeros", three_sum([0, 0, 0, 0]), [[0, 0, 0]])

    # heavy duplicates - this is where most people's code breaks
    check("dupes", three_sum([-2, 0, 0, 2, 2]), [[-2, 0, 2]])
    check("dupes/2", three_sum([-1, -1, -1, 2, 2]), [[-1, -1, 2]])

    # too short
    check("short", three_sum([1, 2]), [])
    check("empty", three_sum([]), [])

    # brute force must agree with the optimal one
    import random
    for _ in range(200):
        arr = [random.randint(-8, 8) for _ in range(random.randint(0, 9))]
        a, b = three_sum(arr[:]), three_sum_brute(arr[:])
        if normalise(a) != normalise(b):
            print(f"[FAIL] mismatch on {arr}: {a} vs {b}")
            break
    else:
        print("[PASS] brute force agrees on 200 random arrays")
