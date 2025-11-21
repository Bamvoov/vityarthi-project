import time
import tracemalloc

def mean_of_digits(n):
    if n < 0:
        n = abs(n)
    
    if n == 0:
        return 0.0
        
    total_sum = 0
    count = 0
    
    while n > 0:
        total_sum += n % 10
        n = n // 10
        count += 1
        
    return total_sum / count

if __name__ == "__main__":
    
    test_number = 12345
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = mean_of_digits(test_number)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Calculating mean of digits for {test_number}.")
    print(f"Result: {result}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")

    test_number_2 = 888
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result_2 = mean_of_digits(test_number_2)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_2 = end_time - start_time
    
    print(f"\nCalculating mean of digits for {test_number_2}.")
    print(f"Result: {result_2}")
    print(f"Execution Time: {execution_time_2:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")