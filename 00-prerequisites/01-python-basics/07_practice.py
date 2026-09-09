"""
Topic: Practice problems for Phase 0

HOW TO USE THIS FILE:
    1. Delete the body of a function and replace it with `pass`.
    2. Solve it yourself.
    3. Run `python 07_practice.py` - the tests at the bottom tell you if
       you got it right.
    4. Peek at the original only after you have really tried.

Every solution has its complexity written on top. Get in the habit of
stating it out loud before you write any code.
"""


# ---------------------------------------------------------------- easy

def reverse_list(arr):
    """Reverse without using [::-1] or .reverse().  Time O(n), Space O(1)"""
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


def find_max_min(arr):
    """Max and min in ONE pass.  Time O(n), Space O(1)"""
    if not arr:
        return None, None
    lo = hi = arr[0]
    for x in arr:
        if x < lo:
            lo = x
        if x > hi:
            hi = x
    return lo, hi


def count_vowels(s):
    """Time O(n), Space O(1)"""
    vowels = set("aeiouAEIOU")
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count


def sum_of_digits(n):
    """Time O(log n) - the number of digits.  Space O(1)"""
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def reverse_number(n):
    """1234 -> 4321.  Time O(log n), Space O(1)"""
    sign = -1 if n < 0 else 1
    n = abs(n)
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return sign * rev


def is_palindrome_number(n):
    """Time O(log n), Space O(1)"""
    if n < 0:
        return False
    return n == reverse_number(n)


# -------------------------------------------------------------- medium

def second_largest(arr):
    """
    Second largest DISTINCT value, in one pass.
    Time O(n), Space O(1). Returns None if there is no second value.
    """
    first = second = float('-inf')
    for x in arr:
        if x > first:
            second = first
            first = x
        elif first > x > second:
            second = x
    return None if second == float('-inf') else second


def move_zeroes(arr):
    """
    Push all zeroes to the end, keep the order of the rest.
    Time O(n), Space O(1). This is a two-pointer warm up.
    """
    insert_at = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[insert_at], arr[i] = arr[i], arr[insert_at]
            insert_at += 1
    return arr


def remove_duplicates_sorted(arr):
    """
    Sorted array -> remove duplicates in place, return the new length.
    Time O(n), Space O(1).
    """
    if not arr:
        return 0
    write = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[write - 1]:
            arr[write] = arr[i]
            write += 1
    return write


def is_anagram(a, b):
    """
    Time O(n), Space O(1) - the dict holds at most 26 keys.
    Better than sorting, which is O(n log n).
    """
    if len(a) != len(b):
        return False
    freq = {}
    for ch in a:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in b:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] == 0:
            del freq[ch]
    return len(freq) == 0


def fizzbuzz(n):
    """The classic. Time O(n)."""
    out = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            out.append("FizzBuzz")
        elif i % 3 == 0:
            out.append("Fizz")
        elif i % 5 == 0:
            out.append("Buzz")
        else:
            out.append(str(i))
    return out


# --------------------------------------------------------------- tests

def check(name, got, want):
    status = "PASS" if got == want else "FAIL"
    print(f"[{status}] {name:<24} got={got!r}")
    if got != want:
        print(f"         expected={want!r}")


if __name__ == "__main__":
    check("reverse_list",     reverse_list([1, 2, 3, 4]),        [4, 3, 2, 1])
    check("find_max_min",     find_max_min([3, 1, 4, 1, 5]),     (1, 5))
    check("count_vowels",     count_vowels("programming"),        3)
    check("sum_of_digits",    sum_of_digits(1234),                10)
    check("reverse_number",   reverse_number(1234),               4321)
    check("is_palindrome_num", is_palindrome_number(1221),        True)
    check("second_largest",   second_largest([3, 1, 4, 4, 5]),    4)
    check("second_largest/1", second_largest([7, 7, 7]),          None)
    check("move_zeroes",      move_zeroes([0, 1, 0, 3, 12]),      [1, 3, 12, 0, 0])
    check("remove_dupes",     remove_duplicates_sorted([1, 1, 2, 2, 3]), 3)
    check("is_anagram",       is_anagram("listen", "silent"),     True)
    check("is_anagram/1",     is_anagram("rat", "car"),           False)
    check("fizzbuzz",         fizzbuzz(5),      ["1", "2", "Fizz", "4", "Buzz"])
