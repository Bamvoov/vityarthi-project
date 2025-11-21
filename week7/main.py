import time
import tracemalloc

def lucas_sequence(n):
    a, b = 2, 1
    count = 0
    while count < n:
        if count == 0:
            yield a
        elif count == 1:
            yield b
        else:
            a, b = b, a + b
            yield b
        count += 1

if __name__ == "__main__":
    n_numbers = 30
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    numbers = list(lucas_sequence(n_numbers))
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Generated {n_numbers} Lucas numbers.")
    print(f"Numbers: {numbers}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")