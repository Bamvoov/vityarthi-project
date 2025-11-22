import time
import tracemalloc

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollard_rho(n):
    if n % 2 == 0:
        return 2
    
    x = 2
    y = 2
    d = 1
    f = lambda v: (v * v + 1) % n
    
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)
        
    if d == n:
        return None 
    return d

if __name__ == "__main__":
    
    test_number = 8051 
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    factor = pollard_rho(test_number)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Factorizing {test_number} using Pollard's Rho.")
    print(f"Found factor: {factor}")
    if factor:
        print(f"Other factor: {test_number // factor}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")

    test_number_2 = 10403 
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    factor_2 = pollard_rho(test_number_2)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_2 = end_time - start_time
    
    print(f"\nFactorizing {test_number_2} using Pollard's Rho.")
    print(f"Found factor: {factor_2}")
    print(f"Execution Time: {execution_time_2:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")