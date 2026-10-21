from collections import Counter

def parse_event(line: str) -> dict:
    first_space = line.find(' ')
    second_space = line.find(' ', first_space+1)
    time, level, message = line[:first_space], line[first_space+1:second_space], line[second_space+1:]
    return {"time": time, "level": level, "message": message}

def count_levels(lines: list[str]) -> dict:
    levels_count = dict()
    for line in lines:
        level = parse_event(line)['level']
        levels_count[level] = levels_count.get(level, 0) + 1

    return levels_count

def top_errors(lines: list[str], n: int) -> list:
    return Counter(parse_event(x)['message'] for x in lines if parse_event(x)['level'] == 'ERROR').most_common(n)

def format_report(counts, errors):
    text = f'''\
Отчёт по журналу

BROKEN: {counts['BROKEN']}
DEBUG: {counts['DEBUG']}
ERROR: {counts['ERROR']}
INFO: {counts['INFO']}
WARNING: {counts['WARNING']}

Частые ошибки:
'''

    for error in errors:
        text += f'- {error[0]} — {error[1]}\n'

    return text