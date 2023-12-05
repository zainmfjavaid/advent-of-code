import time

test_file = 'day_1.py'

start = time.perf_counter()
exec(open("solutions/day_1.py").read())
end = time.perf_counter()

print(f'Executing {test_file} took {(end - start) * 1000:.2f}ms')