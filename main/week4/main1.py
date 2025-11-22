import time
import tracemalloc

def count_distinct_prime_factors(n):
    if n <= 1:
        return 0
        
    count = 0
    
    # Check for divisibility by 2
    if n % 2 == 0:
        count += 1
        while n % 2 == 0:
            n //= 2
            
    # Check for odd factors
    i = 3
    while i * i <= n:
        if n % i == 0:
            count += 1
            while n % i == 0:
                n //= i
        i += 2
        
    # If n > 2, the remaining n is a prime factor
    if n > 2:
        count += 1
        
    return count

if __name__ == "__main__":
    
    test_number = 60 # 60 = 2^2 * 3 * 5 (Distinct: 2, 3, 5 -> 3)
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = count_distinct_prime_factors(test_number)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Counting distinct prime factors of {test_number}.")
    print(f"Result: {result}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")

    test_number_2 = 100 # 100 = 2^2 * 5^2 (Distinct: 2, 5 -> 2)
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result_2 = count_distinct_prime_factors(test_number_2)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_2 = end_time - start_time
    
    print(f"\nCounting distinct prime factors of {test_number_2}.")
    print(f"Result: {result_2}")
    print(f"Execution Time: {execution_time_2:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")