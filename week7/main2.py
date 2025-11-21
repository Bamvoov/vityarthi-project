import time
import tracemalloc
import math

def is_perfect_power(n):
    if n <= 3:
        return False
    
    max_base = int(math.sqrt(n)) + 1
    
    for a in range(2, max_base):
        b = 2
        while True:
            try:
                result = a ** b
            except OverflowError:
                break
                
            if result == n:
                return True
            elif result > n:
                break
            b += 1
    return False

if __name__ == "__main__":
    test_number = 125
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = is_perfect_power(test_number)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Checking if {test_number} is a perfect power.")
    print(f"Result: {result}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")

    test_number_false = 126
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result_false = is_perfect_power(test_number_false)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_false = end_time - start_time
    
    print(f"\nChecking if {test_number_false} is a perfect power.")
    print(f"Result: {result_false}")
    print(f"Execution Time: {execution_time_false:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")