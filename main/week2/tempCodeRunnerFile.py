#Question no 4
import sys
import time

def is_prime(x):
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True

def prime_pi(n):
    count = 0
    for i in range(2, n + 1):
        if is_prime(i):
            count += 1
    return count

def memory_usage(*args):
    return sum(sys.getsizeof(v) for v in args)

n = 30
start = time.time()
result = prime_pi(n)

end = time.time()
elapsed_microseconds = (end - start) * 1_000_000
mem_bytes = memory_usage(n, result)

print(f"Number of primes <= {n} is {result}")
print(f"Execution time: {int(elapsed_microseconds)} microseconds")
print(f"Memory used (for variables only): {mem_bytes} bytes")