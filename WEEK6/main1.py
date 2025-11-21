import time
import tracemalloc
import math

def mod_inverse(a, m):
    if m <= 1:
        return None
    
    try:
        inverse = pow(a, -1, m)
        return inverse
    except ValueError:
        return None

if __name__ == "__main__":
    
    a_val = 7
    m_val = 26
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = mod_inverse(a_val, m_val)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Calculating modular inverse of {a_val} mod {m_val}.")
    print(f"Result (x): {result}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")

    
    a_val_no = 4
    m_val_no = 26
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result_no = mod_inverse(a_val_no, m_val_no)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_no = end_time - start_time
    
    print(f"\nCalculating modular inverse of {a_val_no} mod {m_val_no}.")
    print(f"Result (x): {result_no}")
    print(f"Execution Time: {execution_time_no:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")