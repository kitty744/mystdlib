import time
from mylib import progress

total = 20
start_time = time.time()
spinner_index = 0

for i in range(total + 1):
    progress.progress(i, total, prefix="Loading: ", start_time=start_time, spinner_index=spinner_index)
    spinner_index += 1
    time.sleep(0.1)