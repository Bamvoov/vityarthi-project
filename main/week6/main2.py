import time
import tracemalloc
from functools import reduce

def mod_inverse(a, m):
    try:
        return pow(a, -1, m)
    except ValueError:
        return None

def crt(remainders, moduli):
    if len(remainders) != len(moduli):
        return None
    
    M = reduce(lambda a, b: a * b, moduli)
    
    total = 0
    for r_i, m_i in zip(remainders, moduli):
        M_i = M // m_i
        y_i = mod_inverse(M_i, m_i)
        
        if y_i is None:
            return None
        
        total += r_i * M_i * y_i
        
    return total % M

if __name__ == "__main__":
    
    remainders = [2, 3, 2]
    moduli = [3, 5, 7]
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = crt(remainders, moduli)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Solving system of congruences:")
    for r, m in zip(remainders, moduli):
        print(f"x ≡ {r} mod {m}")
    
    print(f"\nResult (x): {result}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")