"""МКР OPI. Завдання 04: Наступна версія за повідомленнями комітів."""


import re

def next_version(current: str, commits: list[str]) -> str:
    if not isinstance(current, str):
        raise ValueError(f"Некоректна версія: {current}")

    m = re.match(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$", current)
    if not m:
        raise ValueError(f"Некоректна версія: {current}")

    major, minor, patch = map(int, m.groups())
    max_level = 0  # 0: без змін, 1: patch, 2: minor, 3: major

    for commit in commits:
        if not isinstance(commit, str):
            raise ValueError(f"Некоректне повідомлення: {commit}")

        lines = commit.split("\n")
        first_line = lines[0]

        pattern = r"^([a-z]+)(?:\s*\([^)]+\))?(!)?:\s+(\S.*)$"
        match = re.match(pattern, first_line)
        if not match:
            raise ValueError(f"Некоректне повідомлення: {commit}")

        c_type, c_breaking_mark, c_desc = match.groups()

        is_breaking = False
        if c_breaking_mark == "!":
            is_breaking = True
        else:
            for line in lines[1:]:
                if line.startswith("BREAKING CHANGE:"):
                    is_breaking = True
                    break

        if is_breaking:
            level = 3
        elif c_type == "feat":
            level = 2
        elif c_type == "fix":
            level = 1
        else:
            level = 0

        if level > max_level:
            max_level = level

    if max_level == 3:
        return f"{major + 1}.0.0"
    elif max_level == 2:
        return f"{major}.{minor + 1}.0"
    elif max_level == 1:
        return f"{major}.{minor}.{patch + 1}"
    else:
        return current