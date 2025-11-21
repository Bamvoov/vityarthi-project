import time
import tracemalloc
import math

def get_phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def get_divisors(n):
    divs = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
    return sorted(list(divs))

def order_mod(a, n):
    if n <= 1 or math.gcd(a, n) != 1:
        return None
        
    phi_n = get_phi(n)
    divisors = get_divisors(phi_n)
    
    for k in divisors:
        if pow(a, k, n) == 1:
            return k
            
    return None

if __name__ == "__main__":
    
    a_val = 3
    n_val = 7
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = order_mod(a_val, n_val)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Finding the order of {a_val} mod {n_val}.")
    print(f"Result (k): {result}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")

    
    a_val_2 = 5
    n_val_2 = 24
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result_2 = order_mod(a_val_2, n_val_2)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_2 = end_time - start_time
    
    print(f"\nFinding the order of {a_val_2} mod {n_val_2}.")
    print(f"Result (k): {result_2}")
    print(f"Execution Time: {execution_time_2:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")