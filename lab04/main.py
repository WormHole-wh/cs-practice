import sys

from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()
# lines = ['Азов;24.5;2026-07-01', 'мусор', 'Азов;25.5;2026-07-02', 'as; 100; ', 'Таганрог;30s;2026-07-01']
total_count = read_valid(lines)

number_of_lines = len(lines)
number_of_lines_read = sum(total_count[1].values())

records = average_by_city(total_count)
best = warmest_city(records)

print(number_of_lines)
print(number_of_lines - number_of_lines_read)
print(f'{best:.1f}')