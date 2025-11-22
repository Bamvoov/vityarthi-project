import time
import tracemalloc
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_carmichael(n):
    if n <= 1 or is_prime(n):
        return False
    
    for a in range(2, n):
        if math.gcd(a, n) == 1:
            if pow(a, n - 1, n) != 1:
                return False
    return True

if __name__ == "__main__":
    
    test_number = 561
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = is_carmichael(test_number)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Checking if {test_number} is a Carmichael number.")
    print(f"Result: {result}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")

    
    test_number_false = 563
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result_false = is_carmichael(test_number_false)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_false = end_time - start_time
    
    print(f"\nChecking if {test_number_false} is a Carmichael number.")
    print(f"Result: {result_false}")
    print(f"Execution Time: {execution_time_false:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")