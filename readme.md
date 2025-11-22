
# CSE1021: Introduction to Problem Solving and Programming - Lab Practicals

This repository contains Python implementations for a comprehensive set of Number Theory and Algorithm practicals. Each script is designed to be self-contained, including performance measurement (execution time and memory tracking).

## Prerequisites

- **Python 3.x**
    
- Standard libraries used: `math`, `time`, `tracemalloc`, `functools`, `random`.
    

## How to Run

Each file is a standalone script. You can run any of them using the python command:

```
python script_name.py
```

## List of Practicals (1 - 34)

|                   |                             |                                                                            |     |
| ----------------- | --------------------------- | -------------------------------------------------------------------------- | --- |
| **Practical No.** | **Script Name**             | **Description**                                                            |     |
| **1**             | `lucas_generator.py`        | Generates the first _n_ numbers of the Lucas sequence using a generator.   |     |
| **2**             | `perfect_power.py`          | Checks if a number can be expressed as _a^b_ (Perfect Power).              |     |
| **3**             | `collatz_sequence.py`       | Calculates the number of steps to reach 1 in the Collatz conjecture.       |     |
| **4**             | `polygonal_numbers.py`      | Returns the _n_-th _s_-gonal number (e.g., triangular, pentagonal).        |     |
| **5**             | `carmichael_number.py`      | Checks if a composite number satisfies the Carmichael condition.           |     |
| **6**             | `mod_inverse.py`            | Finds the Modular Multiplicative Inverse of _a_ modulo _m_.                |     |
| **7**             | `crt_solver.py`             | Solves a system of linear congruences using the Chinese Remainder Theorem. |     |
| **8**             | `quadratic_residue.py`      | Checks if _a_ is a quadratic residue modulo _p_ using Euler's criterion.   |     |
| **9**             | `order_mod.py`              | Finds the multiplicative order of _a_ modulo _n_.                          |     |
| **10**            | `fibonacci_prime.py`        | Checks if a number is both a Fibonacci number and a Prime number.          |     |
| **11**            | `aliquot_sum.py`            | Calculates the sum of proper divisors of a number.                         |     |
| **12**            | `amicable_numbers.py`       | Checks if two numbers are an Amicable pair.                                |     |
| **13**            | `mult_persistence.py`       | Counts steps to reach a single digit by multiplying digits.                |     |
| **14**            | `highly_composite.py`       | Checks if a number is a Highly Composite Number (HCN).                     |     |
| **15**            | `mod_exp.py`                | Efficiently calculates _(base^exponent) % modulus_.                        |     |
| **16**            | `miller_rabin.py`           | Implements the probabilistic Miller-Rabin primality test.                  |     |
| **17**            | `pollard_rho.py`            | Implements Pollard's Rho algorithm for integer factorization.              |     |
| **18**            | `zeta_approx.py`            | Approximates the Riemann Zeta function for a given _s_.                    |     |
| **19**            | `partition_function.py`     | Calculates _p(n)_, the number of ways to partition an integer.             |     |
| **20**            | `factorial.py`              | Calculates the factorial of a number iteratively.                          |     |
| **21**            | `is_palindrome.py`          | Checks if a number reads the same forwards and backwards.                  |     |
| **22**            | `mean_digits.py`            | Calculates the arithmetic mean of the digits of a number.                  |     |
| **23**            | `digital_root.py`           | Repeatedly sums digits until a single digit (Digital Root) is obtained.    |     |
| **24**            | `is_abundant.py`            | Checks if sum of proper divisors is greater than the number.               |     |
| **25**            | `is_deficient.py`           | Checks if sum of proper divisors is less than the number.                  |     |
| **26**            | `is_harshad.py`             | Checks if a number is divisible by the sum of its digits.                  |     |
| **27**            | `is_automorphic.py`         | Checks if the square of a number ends with the number itself.              |     |
| **28**            | `is_pronic.py`              | Checks if a number is the product of two consecutive integers.             |     |
| **29**            | `prime_factors.py`          | Returns a list of all prime factors of a number.                           |     |
| **30**            | `count_distinct_factors.py` | Returns the count of unique prime factors.                                 |     |
| **31**            | `prime_power.py`            | Checks if a number is a prime power (_p^k_).                               |     |
| **32**            | `mersenne_prime.py`         | Checks if _2^p - 1_ is prime (Mersenne Prime).                             |     |
| **33**            | `twin_primes.py`            | Generates all twin prime pairs up to a given limit.                        |     |
| **34**            | `count_divisors.py`         | Returns the total number of positive divisors of a number.                 |     |

## Code Structure

All scripts follow a consistent pattern:

1. **Core Function**: The mathematical algorithm implementation.
    
2. **Helper Functions**: Necessary utilities (e.g., `gcd`, `is_prime`).
    
3. **`if __name__ == "__main__":` Block**:
    
    - Defines test cases.
        
    - Starts `tracemalloc` for memory tracking.
        
    - Starts `time.perf_counter()` for timing.
        
    - Executes the function.
        
    - Prints the result, execution time, and peak memory usage.
        

Few Snapshots of the project :
<img width="1287" height="878" alt="Pasted image 20251122160610" src="https://github.com/user-attachments/assets/73c1a30f-b88f-42c8-a9a8-b32f2db90fd5" />

<img width="1296" height="818" alt="Pasted image 20251122160520" src="https://github.com/user-attachments/assets/4e24f86c-f8a7-4b04-a8dd-307fa4bdfe4c" />

<img width="758" height="729" alt="Pasted image 20251122160427" src="https://github.com/user-attachments/assets/1ae36a7e-8001-43de-8279-efe06e86d354" />

<img width="780" height="791" alt="Pasted image 20251122160410" src="https://github.com/user-attachments/assets/2b3c30df-598d-4f0a-8ef6-c6e2ebb20284" />

<img width="644" height="554" alt="Pasted image 20251122155639" src="https://github.com/user-attachments/assets/fd5c4749-5cc9-43c3-ab53-57063789349a" />

<img width="641" height="815" alt="Pasted image 20251122155619" src="https://github.com/user-attachments/assets/ad86630e-8aa6-4e24-863c-c469025cf0b4" />

<img width="627" height="835" alt="Pasted image 20251122155600" src="https://github.com/user-attachments/assets/45022326-721a-461e-af51-b6b9199528fe" />

<img width="835" height="742" alt="Pasted image 20251122155512" src="https://github.com/user-attachments/assets/53e2bf1d-b8a4-4655-b480-05ecdbd68408" />

<img width="837" height="718" alt="Pasted image 20251122155441" src="https://github.com/user-attachments/assets/6c3d8cfd-6866-41f7-ab3a-98a444d656e7" />

<img width="528" height="776" alt="Pasted image 20251122155402" src="https://github.com/user-attachments/assets/c5f86fb2-f0c5-4e65-a6fb-8dca26c629d1" />

<img width="972" height="608" alt="Pasted image 20251122155251" src="https://github.com/user-attachments/assets/2cf228e2-8e70-4d49-8bf2-6a2e68ad16dc" />

<img width="976" height="467" alt="Pasted image 20251122155232" src="https://github.com/user-attachments/assets/8dc1e391-633a-4504-857d-88bb58b85cf1" />

