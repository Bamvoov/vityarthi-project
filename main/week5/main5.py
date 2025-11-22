import time
import tracemalloc

def mod_exp(base, exponent, modulus):
    if modulus == 1:
        return 0
    return pow(base, exponent, modulus)

if __name__ == "__main__":
    
    base = 3
    exponent = 4
    modulus = 7
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = mod_exp(base, exponent, modulus)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Calculating ({base}^{exponent}) % {modulus}")
    print(f"Result: {result}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")

    
    base_2 = 5
    exponent_2 = 123456
    modulus_2 = 13
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result_2 = mod_exp(base_2, exponent_2, modulus_2)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_2 = end_time - start_time
    
    print(f"\nCalculating ({base_2}^{exponent_2}) % {modulus_2}")
    print(f"Result: {result_2}")
    print(f"Execution Time: {execution_time_2:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")