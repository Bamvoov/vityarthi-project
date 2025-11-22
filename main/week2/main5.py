import time, sys

n = int(input("Enter a number: "))

# start time
start_time = time.time()

sum_divisors = 0
for i in range(1, n + 1):
    if n % i == 0:
        sum_divisors += i

# end time
end_time = time.time()

print("Sum of divisors of", n, "is:", sum_divisors)

# execution time
execution_time = end_time - start_time
print("Execution Time:", execution_time, "seconds")

# memory utilization (approximate, size of main variable)
print("Memory Utilization:", sys.getsizeof(sum_divisors), "bytes")