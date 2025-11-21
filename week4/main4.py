import time
import tracemalloc

def twin_primes(limit):
    if limit < 3:
        return []
        
    # Sieve of Eratosthenes to find primes up to limit
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
                
    primes = [i for i, prime in enumerate(is_prime) if prime]
    
    # Find twin pairs (p, p+2)
    twins = []
    for i in range(len(primes) - 1):
        if primes[i+1] - primes[i] == 2:
            twins.append((primes[i], primes[i+1]))
            
    return twins

if __name__ == "__main__":
    
    limit_val = 50
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = twin_primes(limit_val)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Generating twin prime pairs up to {limit_val}.")
    print(f"Result: {result}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")