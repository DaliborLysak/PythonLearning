import time

start_time = time.time()

value = 2**1000000000

end_time = time.time()
duration = end_time - start_time
print(f"Computation took {duration:.6f} seconds")