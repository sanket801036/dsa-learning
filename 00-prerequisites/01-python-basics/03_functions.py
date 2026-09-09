"""
Topic: Functions, arguments, return, mutable vs immutable

Mutable vs immutable is the #1 silent bug in DSA code.
If you do not get this, your backtracking answers will be wrong and you
will not know why.
"""


def basics():
    def add(a, b):
        return a + b

    def greet(name, greeting="hello"):     # default argument
        return f"{greeting}, {name}"

    print(add(2, 3))
    print(greet("sanket"))
    print(greet("sanket", "hi"))

    # Return more than one value (it is really a tuple)
    def min_max(nums):
        return min(nums), max(nums)

    lo, hi = min_max([4, 1, 9, 2])
    print(lo, hi)


def mutable_vs_immutable():
    """
    int, float, str, tuple  -> immutable (cannot change in place)
    list, dict, set         -> mutable   (CAN change in place)
    """

    def change_int(x):
        x = 100                 # makes a NEW int, original untouched
        return x

    def change_list(arr):
        arr.append(100)         # changes the ORIGINAL list

    n = 5
    change_int(n)
    print("int after:", n)      # 5  <- unchanged

    a = [1, 2]
    change_list(a)
    print("list after:", a)     # [1, 2, 100]  <- CHANGED


def copy_trap():
    """This bites everyone once. Better it bites you here."""
    a = [1, 2, 3]
    b = a                       # NOT a copy - both names point to the same list
    b.append(4)
    print(a)                    # [1, 2, 3, 4]  <- 'a' changed too!

    a = [1, 2, 3]
    b = a.copy()                # real copy (also works: a[:] or list(a))
    b.append(4)
    print(a)                    # [1, 2, 3]  <- safe


def default_argument_trap():
    """
    A default list is created ONCE, not on every call.
    This is a classic interview gotcha.
    """
    def bad(x, arr=[]):
        arr.append(x)
        return arr

    print(bad(1))       # [1]
    print(bad(2))       # [1, 2]   <- surprise! the old list is still there

    def good(x, arr=None):
        if arr is None:
            arr = []
        arr.append(x)
        return arr

    print(good(1))      # [1]
    print(good(2))      # [2]   <- correct


def why_this_matters_in_dsa():
    """
    In backtracking you build a 'path' list and store it in the answer.
    If you append the list itself, every answer points to the SAME list,
    and at the end they all look identical (usually empty).
    You must append a COPY: path[:] or path.copy()
    """
    result_wrong, result_right = [], []
    path = []

    for x in [1, 2, 3]:
        path.append(x)
        result_wrong.append(path)       # BUG: stores a reference
        result_right.append(path[:])    # correct: stores a snapshot

    print("wrong:", result_wrong)       # all three are the full list
    print("right:", result_right)       # [1], [1,2], [1,2,3]


if __name__ == "__main__":
    print("--- basics ---");            basics()
    print("\n--- mutable ---");         mutable_vs_immutable()
    print("\n--- copy trap ---");       copy_trap()
    print("\n--- default arg trap ---"); default_argument_trap()
    print("\n--- why it matters ---");  why_this_matters_in_dsa()
