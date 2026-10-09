import sys

def parse_record(line: str) -> dict:
    if not line.strip():
        return None

    par = line.split(";")

    if len(par) != 3:
        raise ValueError(...)

    city, temp, date = [i.strip() for i in line.split(";")]

    if not city or not date:
        raise ValueError(...)

    try:
        temp = float(temp.replace(',', '.'))
    except ValueError:
        raise ValueError(...)

    return {'city': city, 'temperature': temp, 'date': date}


def average_by_city(data: list[dict]) -> dict:
    total = {}
    count = {}
    for line in data:
        city = line['city']
        temp = line['temperature']

        total[city] = total.get(city, 0) + float(temp)
        count[city] = count.get(city, 0) + 1

    records = dict()
    for city in total:
        records[city] = total[city] / count[city]
    return records

def read_valid(lines: list[str]) -> list[dict]:
    data = []
    for line in lines:
        try:
            record = parse_record(line)
            if record is not None:
                data.append(record)

        except ValueError:
            continue
    return data

def warmest_city(records: list[dict]) -> str:
    best = ""
    best_temp = float('-inf')
    for city, average_temp in sorted(records.items()):
        if best == "" or average_temp > best_temp:
            best = city
            best_temp = average_temp
    return best_temp