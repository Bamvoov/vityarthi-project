import time
import tracemalloc

def is_quadratic_residue(a, p):
    if p <= 1:
        return False
    
    a = a % p
    if a == 0:
        return True
        
    if p == 2:
        return a == 1

    exponent = (p - 1) // 2
    result = pow(a, exponent, p)
    
    return result == 1

if __name__ == "__main__":
    
    a_res = 2
    p_mod = 7
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = is_quadratic_residue(a_res, p_mod)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Checking if {a_res} is a quadratic residue mod {p_mod}.")
    print(f"Result: {result}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")

    
    a_non_res = 3
    p_mod_non = 7
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result_non = is_quadratic_residue(a_non_res, p_mod_non)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_non = end_time - start_time
    
    print(f"\nChecking if {a_non_res} is a quadratic residue mod {p_mod_non}.")
    print(f"Result: {result_non}")
    print(f"Execution Time: {execution_time_non:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")