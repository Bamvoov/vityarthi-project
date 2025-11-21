import time
import tracemalloc

def polygonal_number(s, n):
    if s < 3 or n < 1:
        return None
    
    numerator = ((s - 2) * n**2) - ((s - 4) * n)
    result = numerator // 2
    return result

if __name__ == "__main__":
    
    s_sides = 5
    n_term = 10
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result_number = polygonal_number(s_sides, n_term)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Calculating the {n_term}-th {s_sides}-gonal number.")
    print(f"Result: {result_number}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")

    
    s_sides_tri = 3
    n_term_tri = 12
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result_tri = polygonal_number(s_sides_tri, n_term_tri)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_tri = end_time - start_time
    
    print(f"\nCalculating the {n_term_tri}-th {s_sides_tri}-gonal (Triangular) number.")
    print(f"Result: {result_tri}")
    print(f"Execution Time: {execution_time_tri:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")