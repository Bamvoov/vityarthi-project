import time
import tracemalloc
import math

def get_divisor_count(n):
    if n == 0:
        return 0
    
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
    return count

def is_highly_composite(n):
    if n <= 1:
        return False
        
    divisor_count_n = get_divisor_count(n)
    
    for i in range(1, n):
        if get_divisor_count(i) >= divisor_count_n:
            return False
            
    return True

if __name__ == "__main__":
    
    test_number = 12
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = is_highly_composite(test_number)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Checking if {test_number} is a highly composite number.")
    print(f"Result: {result}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")

    
    test_number_2 = 10
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result_2 = is_highly_composite(test_number_2)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_2 = end_time - start_time
    
    print(f"\nChecking if {test_number_2} is a highly composite number.")
    print(f"Result: {result_2}")
    print(f"Execution Time: {execution_time_2:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")