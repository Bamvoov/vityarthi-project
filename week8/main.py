import time
import tracemalloc
import random

def is_prime_miller_rabin(n, k=5):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0: return False

    # Find r and d such that n - 1 = 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Perform k rounds of testing
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
            
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
            
    return True

if __name__ == "__main__":
    
    test_prime = 104729 
    rounds = 10
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = is_prime_miller_rabin(test_prime, k=rounds)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Checking if {test_prime} is prime using Miller-Rabin ({rounds} rounds).")
    print(f"Result: {result}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")

    test_composite = 561 
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result_comp = is_prime_miller_rabin(test_composite, k=rounds)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_comp = end_time - start_time
    
    print(f"\nChecking if {test_composite} is prime using Miller-Rabin ({rounds} rounds).")
    print(f"Result: {result_comp}")
    print(f"Execution Time: {execution_time_comp:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")