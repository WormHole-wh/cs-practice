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

def parse_settings(lines: list[str]) -> dict:
    pass

def merge_by_key(rows: list[dict], extra: dict, key: str = id) -> list[dict]:
    pass

def records_to_json(records: list[dict]) -> str:
    pass