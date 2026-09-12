"""
Topic: Two pointers - built up from 2Sum

Read this BEFORE 3Sum. 3Sum is just this trick with one extra loop on top.

The whole idea in one line:
    On a SORTED array, put one pointer at the left and one at the right.
    The sum tells you which pointer to move. No guessing, no nested loop.
"""


# ------------------------------------------------------- step 1: brute force

def two_sum_brute(nums, target):
    """
    Check every pair.
    Time  O(n^2)
    Space O(1)

    Always write this first in an interview. It proves you understand the
    problem. THEN you optimise.
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# ------------------------------------------------------- step 2: hashmap

def two_sum_hashmap(nums, target):
    """
    Unsorted array, need INDICES back.
    Time  O(n)
    Space O(n)

    Key insight: instead of searching for the partner, remember what you
    have already seen. For each number, its partner is (target - number).
    """
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i
    return []


# --------------------------------------------------- step 3: two pointers

def two_sum_sorted(nums, target):
    """
    SORTED array, need the VALUES back.
    Time  O(n)
    Space O(1)   <- this is the win over the hashmap

    WHY it works (this is the part you must understand, not memorise):

        nums = [-4, -1, 0, 1, 2]   target = 1
                 L            R

        sum = -4 + 2 = -2, too SMALL.
        To grow the sum we need a bigger number.
        R is already the biggest available, so R cannot help.
        The only move that increases the sum is L += 1.

        sum too BIG? Same logic mirrored: R -= 1.

    Each step throws away one element permanently, so we touch each
    element at most once -> O(n).

    This ONLY works on a sorted array. On unsorted data "bigger index"
    does not mean "bigger value", so the logic collapses.
    """
    left, right = 0, len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]

        if total == target:
            return [nums[left], nums[right]]
        elif total < target:
            left += 1           # need a bigger sum
        else:
            right -= 1          # need a smaller sum

    return []


# ------------------------------------------------- other two-pointer shapes

def remove_duplicates_sorted(nums):
    """
    Both pointers move the SAME direction here (slow / fast).
    Time O(n), Space O(1). Returns the new length.
    """
    if not nums:
        return 0
    slow = 1
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow - 1]:
            nums[slow] = nums[fast]
            slow += 1
    return slow


def is_palindrome_two_pointer(s):
    """Classic opposite-ends walk. Time O(n), Space O(1)."""
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def container_with_most_water(height):
    """
    Move the SHORTER wall inward - the taller one can never be the
    bottleneck, so moving it can only lose width for no gain.
    Time O(n), Space O(1).
    """
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        width = right - left
        best = max(best, width * min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best


# --------------------------------------------------------------- tests

def check(name, got, want):
    print(f"[{'PASS' if got == want else 'FAIL'}] {name:<26} got={got!r}")
    if got != want:
        print(f"         expected={want!r}")


if __name__ == "__main__":
    check("two_sum_brute",   two_sum_brute([2, 7, 11, 15], 9),      [0, 1])
    check("two_sum_hashmap", two_sum_hashmap([3, 2, 4], 6),         [1, 2])
    check("two_sum_sorted",  two_sum_sorted([-4, -1, 0, 1, 2], 1),  [-1, 2])
    check("two_sum_sorted/1", two_sum_sorted([1, 2, 3], 100),       [])
    check("remove_dupes",    remove_duplicates_sorted([1, 1, 2, 3, 3]), 3)
    check("palindrome",      is_palindrome_two_pointer("racecar"),  True)
    check("container",       container_with_most_water([1,8,6,2,5,4,8,3,7]), 49)

    print("\nWhen to reach for two pointers:")
    print("  - array is sorted (or you can sort it)")
    print("  - you are looking for a PAIR / TRIPLET with some sum")
    print("  - you want O(1) space instead of a hashmap")
    print("  - you are shrinking a window from both ends")
