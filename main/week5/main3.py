import time
import tracemalloc
from functools import reduce

def multiplicative_persistence(n):
    if n < 0:
        n = abs(n)
        
    count = 0
    while n >= 10:
        digits = [int(d) for d in str(n)]
        n = reduce(lambda x, y: x * y, digits)
        count += 1
    return count

if __name__ == "__main__":
    
    test_number = 77
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = multiplicative_persistence(test_number)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Calculating multiplicative persistence of {test_number}.")
    print(f"Result (steps): {result}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")

    
    test_number_2 = 123
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result_2 = multiplicative_persistence(test_number_2)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_2 = end_time - start_time
    
    print(f"\nCalculating multiplicative persistence of {test_number_2}.")
    print(f"Result (steps): {result_2}")
    print(f"Execution Time: {execution_time_2:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")