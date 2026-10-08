import sys

from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()
total_count = read_valid(lines)

records = average_by_city(total_count)
best = warmest_city(records)

print(len(lines))
print(len(lines) - len(records))
print(best)