import sys

def parse_record(line: str) -> dict:
    if not line.strip():
        raise ValueError(...)

    par = line.split(";")

    if len(par) != 3:
        raise ValueError(...)

    city, temp, date = [i.strip() for i in line.split(";")]

    if not city or not date:
        raise ValueError(...)

    try:
        temp = float(temp)
    except ValueError:
        raise ValueError(...)

    return {'city': city, 'temperature': temp, 'date': date}


def average_by_city(records: list[dict]) -> dict:
    total, count = records
    records = dict()
    for city in total:
        records[city] = total[city] / count[city]
    return records

def read_valid(lines: list[str]) -> list[dict]:
    total = {}
    count = {}
    count_skip_lines = 0
    for line in lines:
        try:
            line = parse_record(line)
        except ValueError:
            continue

        if line:
            city = line['city']
            temp = line['temperature']

            total[city] = total.get(city, 0) + float(temp)
            count[city] = count.get(city, 0) + 1
    return [total, count]

def warmest_city(records: list[dict]) -> str:
    best = ""
    best_temp = float('-inf')
    for city, average_temp in sorted(records.items()):
        if best == "" or average_temp > best_temp:
            best = city
            best_temp = average_temp
    return best_temp