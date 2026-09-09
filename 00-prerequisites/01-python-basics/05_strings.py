"""
Topic: Strings

The big rule: strings in Python are IMMUTABLE.
s[0] = 'x' is an error. Every "change" makes a brand new string.
That single fact decides the complexity of half your string solutions.
"""


def immutability():
    s = "hello"
    print(s[0], s[-1])

    # s[0] = 'H'          # TypeError - cannot change in place
    s2 = "H" + s[1:]      # make a new one instead
    print(s2)

    # THE classic mistake: building a string in a loop
    # Each += copies the whole string -> O(n^2) total
    slow = ""
    for ch in "abcdef":
        slow += ch                      # bad on large input

    # Correct: collect in a list, join once -> O(n)
    parts = []
    for ch in "abcdef":
        parts.append(ch)
    fast = "".join(parts)

    print(slow, fast)


def methods():
    s = "  Hello World  "

    print(repr(s.strip()))          # removes spaces from both ends
    print(s.strip().lower())        # 'hello world'
    print(s.strip().upper())
    print(s.strip().split())        # ['Hello', 'World']  splits on whitespace
    print("a,b,c".split(","))       # ['a', 'b', 'c']
    print("-".join(['a', 'b', 'c']))# 'a-b-c'
    print("hello".replace("l", "L"))
    print("hello".find("ll"))       # 2, or -1 if not found
    print("hello".count("l"))       # 2
    print("hello".startswith("he"), "hello".endswith("lo"))

    # Character checks - useful in parsing questions
    print("a".isalpha(), "1".isdigit(), "a1".isalnum(), " ".isspace())


def char_and_ord():
    """
    ord() gives the ASCII number, chr() gives the character back.
    This is how you map 'a'..'z' to an array of size 26.
    """
    print(ord('a'), ord('z'), ord('A'), ord('0'))    # 97 122 65 48
    print(chr(97), chr(65))                          # a A

    # Frequency array for lowercase letters - no dict needed
    s = "banana"
    freq = [0] * 26
    for ch in s:
        freq[ord(ch) - ord('a')] += 1

    for i in range(26):
        if freq[i] > 0:
            print(chr(i + ord('a')), freq[i], end="   ")
    print()


def common_problems():
    # Reverse a string
    s = "hello"
    print(s[::-1])

    # Palindrome check
    def is_palindrome(s):
        s = "".join(ch.lower() for ch in s if ch.isalnum())
        return s == s[::-1]

    print(is_palindrome("A man, a plan, a canal: Panama"))   # True
    print(is_palindrome("hello"))                            # False

    # Count vowels
    print(sum(1 for ch in "programming" if ch in "aeiou"))

    # Are two strings anagrams?
    def is_anagram(a, b):
        return sorted(a) == sorted(b)       # O(n log n), fine to start

    print(is_anagram("listen", "silent"))

    # First non-repeating character
    def first_unique(s):
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        for ch in s:
            if freq[ch] == 1:
                return ch
        return None

    print(first_unique("swiss"))    # w


if __name__ == "__main__":
    print("--- immutability ---");  immutability()
    print("\n--- methods ---");     methods()
    print("\n--- ord/chr ---");     char_and_ord()
    print("\n--- problems ---");    common_problems()
