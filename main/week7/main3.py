import time
import tracemalloc

def collatz_length(n):
    if n <= 0:
        return 0
    
    length = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    return length

if __name__ == "__main__":
    test_number = 27
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result_length = collatz_length(test_number)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Calculating Collatz sequence length for {test_number}.")
    print(f"Result (steps to reach 1): {result_length}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")

    test_number_long = 837799
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result_length_long = collatz_length(test_number_long)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_long = end_time - start_time
    
    print(f"\nCalculating Collatz sequence length for {test_number_long}.")
    print(f"Result (steps to reach 1): {result_length_long}")
    print(f"Execution Time: {execution_time_long:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")