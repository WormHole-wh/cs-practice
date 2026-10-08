import sys

def parse_record(line: str) -> dict:
    city, temp, date = line.split(";")
    return {'city': city, 'temperature': float(temp), 'date': date}

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
        line = parse_record(line)
        city = line['city']
        temp = line['temperature']

        total[city] = total.get(city, 0) + float(temp)
        count[city] = count.get(city, 0) + 1
    return list(total, count)

def warmest_city(records: list[dict]) -> str:
    best = ""
    best_temp = float('-inf')
    for city, average_temp in records:
        if best == "" or average_temp >= best_temp:
            best = min(city, best)
            best_temp = average_temp
    return best