import time
import random

size = 10000
data = list(range(size))
data_set = set(data)

search_elements = random.sample(data, 1000)

# Search in list
start_time = time.time()
for elem in search_elements:
    _ = elem in data
list_duration = time.time() - start_time

# Search in set
start_time = time.time()
for elem in search_elements:
    _ = elem in data_set
set_duration = time.time() - start_time

print(f"List search time: {list_duration:.6f} seconds")
print(f"Set search time:  {set_duration:.6f} seconds")
print(f"Set is {list_duration / set_duration:.2f} times faster than list.")
