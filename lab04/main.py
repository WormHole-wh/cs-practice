import sys

from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()
# lines = ['Азов;24.5;2026-07-01', 'мусор', 'Азов;25.5;2026-07-02', 'as; 100; ', 'Таганрог;30;2026-07-01']
data = read_valid(lines)
records = average_by_city(data)
best = warmest_city(records)

number_of_lines = len(lines)
number_of_lines_read = len(data)

print(number_of_lines_read)
print(number_of_lines - number_of_lines_read)
print(f'{records[best]:.1f}')