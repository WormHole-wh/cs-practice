from json import dumps

def csv_to_records(text: str) -> list[dict]:
    lines = text.split('\n')
    titles = lines[0].split(',')
    len_titles = len(titles)
    res = list()
    for line in lines[1:]:
        my_dict = dict()
        for i in range(len_titles):
            my_dict[titles[i]] = line[i]

        res.append(my_dict)

    return res


def auto_to_type(value: str):
    if value.lower() == 'true':
        return True
    if value.lower() == 'false':
        return False

    try:
        return int(value)
    except ValueError:
        pass

    try:
        return float(value)
    except ValueError:
        pass

    return value


def parse_settings(lines: list[str]) -> dict:
    res = dict()
    f = 0

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if line[0] == '#':
            continue

        if line == 'columns:':
            columns = []
            f = 1

        if f and line[0] == '-':
            columns.append(auto_to_type(line[1:].strip()))
            continue

        key, value = [i.strip() for i in line.split(':')]
        res[key] = auto_to_type(value)

    res['columns'] = columns

    return res


def merge_by_key(rows: list[dict], extra: dict, key: str = id) -> list[dict]:
        res = []
        for record in rows:
            _record = record.copy()

            key_value = record.get(key)

            if key_value in extra:
                data = extra[key_value]
                for key, value in data.items():
                    if key not in _record:
                        _record[key] = value

            res.append(_record)
        return res


def records_to_json(records: list[dict]) -> str:
    return dumps(records, ensure_ascii=False, indent=2, sort_keys=True)