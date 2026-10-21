def parse_event(line: str) -> dict:
    first_space = line.find(' ')
    second_space = line.find(' ', first_space+1)
    time, level, message = line[:first_space], line[first_space+1:second_space], line[second_space+1:]
    return {"time": time, "level": level, "message": message}

def count_levels(lines):
    ...

def top_errors(lines, n):
    ...

def format_report(counts, errors):
    ...