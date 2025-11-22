import time
import tracemalloc

def prime_factors(n):
    factors = []
    # Handle divisibility by 2
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
        
    # Handle odd factors
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n = n // i
        i += 2
        
    # If n is a prime greater than 2
    if n > 2:
        factors.append(n)
        
    return factors

if __name__ == "__main__":
    
    test_number = 315 # 315 = 3 * 3 * 5 * 7
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = prime_factors(test_number)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Calculating prime factors of {test_number}.")
    print(f"Result: {result}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")

    test_number_prime = 37
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result_prime = prime_factors(test_number_prime)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_prime = end_time - start_time
    
    print(f"\nCalculating prime factors of {test_number_prime}.")
    print(f"Result: {result_prime}")
    print(f"Execution Time: {execution_time_prime:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")