import time
import tracemalloc
import math

def aliquot_sum(n):
    if n <= 1:
        return 0
    
    total = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            total += i
            if i * i != n:
                total += n // i
    return total

if __name__ == "__main__":
    
    test_number = 220
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = aliquot_sum(test_number)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Calculating aliquot sum of {test_number}.")
    print(f"Result (sum of proper divisors): {result}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")

    
    test_number_2 = 12
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result_2 = aliquot_sum(test_number_2)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_2 = end_time - start_time
    
    print(f"\nCalculating aliquot sum of {test_number_2}.")
    print(f"Result (sum of proper divisors): {result_2}")
    print(f"Execution Time: {execution_time_2:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")