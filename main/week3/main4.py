import time
import tracemalloc
import math

def is_pronic(n):
    if n < 0:
        return False
    
    # A pronic number is the product of two consecutive integers: k * (k + 1)
    # This means n approx k^2, so k approx sqrt(n).
    
    k = int(math.sqrt(n))
    return k * (k + 1) == n

if __name__ == "__main__":
    
    test_number = 56 # 7 * 8
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = is_pronic(test_number)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Checking if {test_number} is a pronic number.")
    print(f"Result: {result}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")

    test_number_false = 50
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result_false = is_pronic(test_number_false)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_false = end_time - start_time
    
    print(f"\nChecking if {test_number_false} is a pronic number.")
    print(f"Result: {result_false}")
    print(f"Execution Time: {execution_time_false:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")