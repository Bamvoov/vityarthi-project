import time
import tracemalloc

def digital_root(n):
    if n < 0:
        n = abs(n)
        
    while n >= 10:
        sum_digits = 0
        while n > 0:
            sum_digits += n % 10
            n = n // 10
        n = sum_digits
        
    return n

if __name__ == "__main__":
    
    test_number = 942
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = digital_root(test_number)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Calculating digital root of {test_number}.")
    print(f"Result: {result}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")

    test_number_2 = 16
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result_2 = digital_root(test_number_2)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_2 = end_time - start_time
    
    print(f"\nCalculating digital root of {test_number_2}.")
    print(f"Result: {result_2}")
    print(f"Execution Time: {execution_time_2:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")