import time
import tracemalloc
import math

def is_prime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_mersenne_prime(p):
    # A Mersenne number is M_p = 2^p - 1
    # This function checks if M_p is prime.
    
    mersenne_number = (2 ** p) - 1
    return is_prime(mersenne_number)

if __name__ == "__main__":
    
    p_val = 5 # 2^5 - 1 = 31
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = is_mersenne_prime(p_val)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Checking if 2^{p_val} - 1 is a Mersenne prime.")
    print(f"Result: {result}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")

    p_val_false = 11 # 2^11 - 1 = 2047 (23 * 89)
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result_false = is_mersenne_prime(p_val_false)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_false = end_time - start_time
    
    print(f"\nChecking if 2^{p_val_false} - 1 is a Mersenne prime.")
    print(f"Result: {result_false}")
    print(f"Execution Time: {execution_time_false:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")