import time
import tracemalloc
import math

def get_proper_divisors_sum(n):
    if n <= 1:
        return 0
    total = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            total += i
            if i * i != n:
                total += n // i
    return total

def is_deficient(n):
    if n <= 0:
        return False
    return get_proper_divisors_sum(n) < n

if __name__ == "__main__":
    
    test_number = 15
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = is_deficient(test_number)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Checking if {test_number} is a deficient number.")
    print(f"Result: {result}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")

    test_number_false = 12
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result_false = is_deficient(test_number_false)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_false = end_time - start_time
    
    print(f"\nChecking if {test_number_false} is a deficient number.")
    print(f"Result: {result_false}")
    print(f"Execution Time: {execution_time_false:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")