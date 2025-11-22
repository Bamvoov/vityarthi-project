import time
import tracemalloc

def is_prime_power(n):
    if n <= 1:
        return False
        
    # Find the smallest prime factor p
    p = 0
    
    # Check 2 first
    if n % 2 == 0:
        p = 2
    else:
        i = 3
        while i * i <= n:
            if n % i == 0:
                p = i
                break
            i += 2
    
    # If no factor found, n is prime (which is a prime power where k=1)
    if p == 0:
        return True
        
    # Divide n by p repeatedly
    while n > 1:
        if n % p != 0:
            return False
        n //= p
        
    return True

if __name__ == "__main__":
    
    test_number = 27 # 3^3
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = is_prime_power(test_number)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Checking if {test_number} is a prime power.")
    print(f"Result: {result}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")

    test_number_false = 12 # 2^2 * 3 (Not a single prime power)
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result_false = is_prime_power(test_number_false)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_false = end_time - start_time
    
    print(f"\nChecking if {test_number_false} is a prime power.")
    print(f"Result: {result_false}")
    print(f"Execution Time: {execution_time_false:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")