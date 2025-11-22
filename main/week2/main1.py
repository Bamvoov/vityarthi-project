import time, sys

def mobius(n):
    if n == 1:
        return 1
    p = 2
    temp = n
    count_primes = 0
    while p * p <= temp:
        if temp % p == 0:
            count_primes += 1
            temp //= p
            if temp % p == 0:
                return 0
        p += 1 if p == 2 else 2
    if temp > 1:
        count_primes += 1
    if count_primes % 2 == 0:
        return 1
    else:
        return -1

n = int(input("Enter a number: "))
start_time = time.time()
result = mobius(n)
end_time = time.time()
execution_time = end_time - start_time
memory_used = sys.getsizeof(result) + sys.getsizeof(n)
print("Mobius function µ({}) = {}".format(n, result))
print("Execution time: {:.10f} seconds".format(execution_time))
print("Memory used: {} bytes".format(memory_used))