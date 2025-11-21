import time
import tracemalloc

def is_automorphic(n):
    if n < 0:
        return False
        
    square = n * n
    
    # Mathematically extract the last digits of the square
    # The number of digits to extract equals the number of digits in n
    
    temp_n = n
    divisor = 1
    while temp_n > 0:
        divisor *= 10
        temp_n //= 10
        
    # Special case for n=0
    if n == 0:
        divisor = 10
        
    last_digits = square % divisor
    
    return last_digits == n

if __name__ == "__main__":
    
    test_number = 25
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = is_automorphic(test_number)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Checking if {test_number} is an automorphic number.")
    print(f"Result: {result}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")

    test_number_false = 7
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result_false = is_automorphic(test_number_false)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_false = end_time - start_time
    
    print(f"\nChecking if {test_number_false} is an automorphic number.")
    print(f"Result: {result_false}")
    print(f"Execution Time: {execution_time_false:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")