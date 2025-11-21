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

def are_amicable(a, b):
    if a == b:
        return False
    return aliquot_sum(a) == b and aliquot_sum(b) == a

if __name__ == "__main__":
    
    a_val, b_val = 220, 284
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = are_amicable(a_val, b_val)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Checking if {a_val} and {b_val} are amicable.")
    print(f"Result: {result}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")

    
    a_val_2, b_val_2 = 100, 200
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result_2 = are_amicable(a_val_2, b_val_2)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_2 = end_time - start_time
    
    print(f"\nChecking if {a_val_2} and {b_val_2} are amicable.")
    print(f"Result: {result_2}")
    print(f"Execution Time: {execution_time_2:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")