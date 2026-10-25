def count_by_extension(paths: list[str]) -> dict[str, int]:
    count_ext = {}
    for path in paths:
        if not path.strip():
            continue

        path = path[path.rfind('/') + 1:]
        last_point = path.rfind('.')

        if last_point in (0, -1):
            ext = ''

        else:
            ext = path[last_point + 1:].lower()
        count_ext[ext] = count_ext.get(ext, 0) + 1

    return count_ext

def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ''
    return max(paths, key=lambda x: x.count('/'))

def human_size(n_bytes: int) -> str:
    if n_bytes < 1024:
        return f'{n_bytes} Б'
    n_bytes /= 1024

    if n_bytes < 1024:
        return f'{n_bytes:.1f} КБ'
    n_bytes /= 1024

    if n_bytes < 1024:
        return f'{n_bytes:.1f} МБ'
    n_bytes /= 1024

    if n_bytes < 1024:
        return f'{n_bytes:.1f} ГБ'
    n_bytes /= 1024

    return f'{n_bytes:.1f} ТБ'