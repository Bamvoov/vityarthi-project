import time
import tracemalloc

def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    
    test_number = 50
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = factorial(test_number)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Calculating factorial of {test_number}.")
    print(f"Result: {result}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")

    test_number_small = 5
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result_small = factorial(test_number_small)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_small = end_time - start_time
    
    print(f"\nCalculating factorial of {test_number_small}.")
    print(f"Result: {result_small}")
    print(f"Execution Time: {execution_time_small:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")