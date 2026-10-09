import sys
from stats import average_by_city, read_valid, warmest_city

lines = [i.strip() for i in sys.stdin.read().splitlines()]

for _ in range(lines.count('')):
    lines.remove('')
data = read_valid(lines)
records = average_by_city(data)
best = warmest_city(records)

number_of_lines = len(lines)
number_of_lines_read = len(data)

print(number_of_lines_read)
print(number_of_lines - number_of_lines_read)
print(f'{records[best]:.1f}')