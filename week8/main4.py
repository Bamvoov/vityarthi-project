import time
import tracemalloc

def partition_function(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
        
    partitions = [0] * (n + 1)
    partitions[0] = 1
    
    for k in range(1, n + 1):
        for i in range(k, n + 1):
            partitions[i] += partitions[i - k]
            
    return partitions[n]

if __name__ == "__main__":
    
    test_number = 5
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = partition_function(test_number)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Calculating partition function p({test_number}).")
    print(f"Result (ways to write sum): {result}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")

    test_number_2 = 60
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result_2 = partition_function(test_number_2)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_2 = end_time - start_time
    
    print(f"\nCalculating partition function p({test_number_2}).")
    print(f"Result (ways to write sum): {result_2}")
    print(f"Execution Time: {execution_time_2:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")