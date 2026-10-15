"""МКР OPI. Завдання 05: План спринту за швидкістю команди."""


import math

def sprint_plan(backlog: list[tuple[str, int]], velocities: list[int]) -> str:
    if (
        not isinstance(velocities, list)
        or len(velocities) == 0
        or any(not isinstance(v, int) or isinstance(v, bool) or v < 1 for v in velocities)
    ):
        raise ValueError("Некоректна історія швидкості")

    if not isinstance(backlog, list):
        raise ValueError("Некоректний беклог")

    seen_names = set()
    for item in backlog:
        if (
            not isinstance(item, (tuple, list))
            or len(item) != 2
            or not isinstance(item[0], str)
            or not item[0]
            or not isinstance(item[1], int)
            or isinstance(item[1], bool)
            or item[1] < 1
        ):
            raise ValueError("Некоректний беклог")

        name, size = item
        if name in seen_names:
            raise ValueError(f"Дубль у беклозі: {name}")
        seen_names.add(name)

    last_v = velocities[-3:]
    capacity = sum(last_v) // len(last_v)

    need_split = []
    ready_items = []
    for name, size in backlog:
        if size > 8:
            need_split.append(name)
        else:
            ready_items.append((name, size))

    in_sprint = []
    current_sum = 0
    for name, size in ready_items:
        if current_sum + size <= capacity:
            in_sprint.append(name)
            current_sum += size
        else:
            break

    total_ready_size = sum(size for _, size in ready_items)
    if total_ready_size == 0:
        sprints_needed = 0
    else:
        sprints_needed = math.ceil(total_ready_size / capacity)

    line1 = f"Місткість: {capacity} б."
    if in_sprint:
        line2 = f"У спринт: {', '.join(in_sprint)} ({current_sum} б.)"
    else:
        line2 = "У спринт: немає (0 б.)"

    if need_split:
        line3 = f"Потребують розбиття: {', '.join(need_split)}"
    else:
        line3 = "Потребують розбиття: немає"

    line4 = f"Спринтів до завершення готових пунктів: {sprints_needed}"

    return f"{line1}\n{line2}\n{line3}\n{line4}"