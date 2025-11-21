import time
import tracemalloc

def is_harshad(n):
    if n <= 0:
        return False
    
    original_n = n
    sum_digits = 0
    while n > 0:
        sum_digits += n % 10
        n //= 10
        
    return original_n % sum_digits == 0

if __name__ == "__main__":
    
    test_number = 18
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = is_harshad(test_number)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Checking if {test_number} is a Harshad number.")
    print(f"Result: {result}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")

    test_number_false = 19
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result_false = is_harshad(test_number_false)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_false = end_time - start_time
    
    print(f"\nChecking if {test_number_false} is a Harshad number.")
    print(f"Result: {result_false}")
    print(f"Execution Time: {execution_time_false:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")