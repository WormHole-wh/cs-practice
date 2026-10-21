from collections import Counter

def parse_event(line: str) -> dict:
    line = line.strip().split(' ', 2)
    if len(line) == 3:
        time, level, message = line
        if level in ('DEBUG', 'INFO', 'WARNING', 'ERROR'):
            if time.strip() and message.strip():
                return {"time": time, "level": level, "message": message}

    raise ValueError

def count_levels(lines: list[str]) -> dict:
    levels_count = dict()
    for line in lines:
        if not line.strip():
            continue
        try:
            level = parse_event(line)['level']
            levels_count[level] = levels_count.get(level, 0) + 1
        except ValueError:
            levels_count['BROKEN'] = levels_count.get('BROKEN', 0) + 1

    return levels_count

def top_errors(lines: list[str], n: int) -> list:
    try:
        return Counter(parse_event(x)['message'] for x in lines if parse_event(x)['level'] == 'ERROR').most_common(n)
    except ValueError:
        _lines = list()
        for x in lines:
            try:
                line = parse_event(x)
            except ValueError:
                continue
            if line['level'] == 'ERROR':
                _lines.append(line['message'])
        return Counter(_lines).most_common(n)

def format_report(counts, errors):
    text = f'Отчёт по журналу\n\n'
    for level in sorted(counts):
        text += f'{level}: {counts[level]}\n'

    text += '\nЧастые ошибки:\n'
    for error in errors:
        text += f'- {error[0]} — {error[1]}\n'

    return text