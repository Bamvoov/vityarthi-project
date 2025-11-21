import time
import tracemalloc

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_perfect_square(k):
    if k < 0:
        return False
    s = int(k**0.5)
    return s * s == k

def is_fibonacci(n):
    if n < 0:
        return False
    
    test_1 = 5 * n**2 + 4
    test_2 = 5 * n**2 - 4
    return is_perfect_square(test_1) or is_perfect_square(test_2)

def is_fibonacci_prime(n):
    return is_prime(n) and is_fibonacci(n)

if __name__ == "__main__":
    
    test_number = 13
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result = is_fibonacci_prime(test_number)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    
    print(f"Checking if {test_number} is a Fibonacci Prime.")
    print(f"Result: {result}")
    print(f"Execution Time: {execution_time:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")

    
    test_number_false = 21
    
    tracemalloc.start()
    start_time = time.perf_counter()
    
    result_false = is_fibonacci_prime(test_number_false)
    
    end_time = time.perf_counter()
    current_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    execution_time_false = end_time - start_time
    
    print(f"\nChecking if {test_number_false} is a Fibonacci Prime.")
    print(f"Result: {result_false}")
    print(f"Execution Time: {execution_time_false:.9f} seconds")
    print(f"Peak Memory Usage: {peak_mem / 1024:.2f} KiB")