# 2. Maths for DSA

You do not need advanced maths. You need these specific tools.

## Checklist

### Number theory
- [ ] Prime check in O(sqrt(n))
- [ ] Sieve of Eratosthenes
- [ ] Prime factorisation
- [ ] All divisors of n in O(sqrt(n))
- [ ] GCD using Euclidean algorithm
- [ ] LCM using `a * b // gcd(a, b)`

### Modular arithmetic
- [ ] Why answers are asked "modulo 1e9+7"
- [ ] `(a + b) % m`, `(a * b) % m`
- [ ] Binary exponentiation (power in O(log n))

### Digits
- [ ] Extract digits using `% 10` and `// 10`
- [ ] Count digits, sum of digits, reverse a number
- [ ] Palindrome number, Armstrong number

### Combinatorics
- [ ] Factorial (loop and recursive)
- [ ] nCr and nPr
- [ ] Basic counting: how many subsets does a set of n items have

### Bit manipulation
- [ ] Binary representation, `bin()`
- [ ] AND, OR, XOR, NOT, left shift, right shift
- [ ] Check if the i-th bit is set: `n & (1 << i)`
- [ ] Set / clear / toggle the i-th bit
- [ ] `n & (n - 1)` removes the lowest set bit
- [ ] `n & -n` gives the lowest set bit
- [ ] Check power of two: `n > 0 and n & (n - 1) == 0`
- [ ] Count set bits
- [ ] XOR trick: `a ^ a = 0`, so it finds the single non-repeating number

## Why each one shows up

- GCD -> fraction problems, array problems
- Sieve -> any question about primes in a range
- Binary exponentiation -> large powers without overflow or TLE
- XOR -> "find the number that appears once"
- `n & (n-1)` -> counting bits, power-of-two checks
