import sys

from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()
total = {}
count = {}
count_skip_lines = 0
for line in lines:
    city, temp, date = read_valid(line)
    total[city] = total.get(city, 0) + float(temp)
    count[city] = count.get(city, 0) + 1

best = warmest_city(total, count)

print(len(lines))
print(count_skip_lines)
print(average_by_city(total, count, best))