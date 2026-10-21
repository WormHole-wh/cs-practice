from logstats import *

path = input().strip()
with open(path, encoding='utf-8') as log:
    lines = list()
    read_lines = 0
    for line in log:
        if not line.strip():
            continue
        read_lines += 1
        lines.append(line)

    counts = count_levels(lines)
    print(f'{read_lines}\n{counts["ERROR"]}\n{counts["BROKEN"]}')
    errors = top_errors(lines, 3)

    with open("report.txt", "w", encoding="utf-8") as f:
        f.writelines(format_report(counts, errors))
