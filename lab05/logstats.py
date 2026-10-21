from collections import Counter

def parse_event(line: str) -> dict:
    line = line.strip().split(' ', 2)
    if len(line) == 3:
        time, level, message = line
        if level in ('DEBUG', 'INFO', 'WARNING', 'ERROR'):
            return {"time": time, "level": level, "message": message}

    return {"time": None, "level": 'BROKEN', "message": None}

def count_levels(lines: list[str]) -> dict:
    levels_count = dict()
    for line in lines:
        level = parse_event(line)['level']
        levels_count[level] = levels_count.get(level, 0) + 1

    return levels_count

def top_errors(lines: list[str], n: int) -> list:
    return Counter(parse_event(x)['message'] for x in lines if parse_event(x)['level'] == 'ERROR').most_common(n)

def format_report(counts, errors):
    text = f'Отчёт по журналу\n'
    for level in sorted(counts):
        text += f'{level}: {counts[level]}\n'

    text += '\nЧастые ошибки:\n'
    for error in errors:
        text += f'- {error[0]} — {error[1]}\n'

    return text