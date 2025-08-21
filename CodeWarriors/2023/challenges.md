# Challenges

## Challenge 2

### Task

The aim of this task is to decompose $n!$ (n factorial) into its prime factors.

### Examples

* $n = 12 \to 2^{10} \cdot 3^5 \cdot 5^2 \cdot 7 \cdot 11$
  * Since 12! is divisible by 2 ten times, by 3 five times, by 5 two times, by 7 one time, and by 11 one time.
* $n = 22 \to 2^{19} \cdot 3^9 \cdot 5^4 \cdot 7^3 \cdot 11^2 \cdot 13 \cdot 17 \cdot 19$
* $n = 25 \to 2^{22} \cdot 3^{10} \cdot 5^6 \cdot 7^3 \cdot 11^2 \cdot 13 \cdot 17 \cdot 19 \cdot 23$

Prime numbers should be in increasing order. When the exponent of a prime is 1 don't put the exponent.

### Requirements

* The function is `decomp(n)` and should return the decomposition of $n!$ into its prime factors in increasing order of the primes, as a string.
* Factorial can be a very big number (4000! has 12674 digits, n can go from 300 to 4000).
* The returned string is not permitted to contain any redundant trailing white space.

### Form

```python
def decomp(n):
    # your code here
```
