import time
import tracemalloc

def zeta_approx(s, terms):
    if s <= 1:
        return None 
        
    total = 0.0
    for n in range(1, terms + 1):
        total += 1 / (n ** s)
        
    return total

if __name__ == "__main__":
    
    s_val = 2
    terms_count = 100000
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = zeta_approx(s_val, terms_count)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    # The true value of Zeta(2) is (pi^2) / 6 approx 1.644934
    true_val_approx = 1.6449340668
    
    print(f"Approximating Riemann Zeta({s_val}) using {terms_count} terms.")
    print(f"Approximation: {result:.10f}")
    print(f"Target Value : {true_val_approx:.10f}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")

    s_val_4 = 4
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result_4 = zeta_approx(s_val_4, terms_count)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_4 = end_time - start_time
    
    # The true value of Zeta(4) is (pi^4) / 90 approx 1.082323
    true_val_4_approx = 1.0823232337
    
    print(f"\nApproximating Riemann Zeta({s_val_4}) using {terms_count} terms.")
    print(f"Approximation: {result_4:.10f}")
    print(f"Target Value : {true_val_4_approx:.10f}")
    print(f"Execution Time: {execution_time_4:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")