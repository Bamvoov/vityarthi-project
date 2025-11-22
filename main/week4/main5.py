import time
import tracemalloc
import math

def count_divisors(n):
    if n <= 0:
        return 0
    
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
    return count

if __name__ == "__main__":
    
    test_number = 24 # Divisors: 1, 2, 3, 4, 6, 8, 12, 24 (Total 8)
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = count_divisors(test_number)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Counting positive divisors of {test_number}.")
    print(f"Result: {result}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")

    test_number_sq = 36 # Divisors: 1, 2, 3, 4, 6, 9, 12, 18, 36 (Total 9)
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result_sq = count_divisors(test_number_sq)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_sq = end_time - start_time
    
    print(f"\nCounting positive divisors of {test_number_sq}.")
    print(f"Result: {result_sq}")
    print(f"Execution Time: {execution_time_sq:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")