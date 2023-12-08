import time

test_file = 'day_4.py'

start = time.perf_counter()
exec(open(f"solutions/{test_file}").read())
end = time.perf_counter()

print(f'Executing {test_file} took {(end - start) * 1000:.2f}ms')