"""МКР OPI. Завдання 08: Триверсійне злиття файла."""


def merge3(base: list[str], ours: list[str], theirs: list[str]) -> str:
    if not (isinstance(base, list) and isinstance(ours, list) and isinstance(theirs, list)):
        raise ValueError("Версії різної довжини")

    if len(base) != len(ours) or len(base) != len(theirs):
        raise ValueError("Версії різної довжини")

    if not base:
        return ""

    result_lines = []
    in_conflict = False
    conflict_ours = []
    conflict_theirs = []

    for b, o, t in zip(base, ours, theirs):
        if o == t:
            is_conflict = False
            resolved = o
        elif o == b:
            is_conflict = False
            resolved = t
        elif t == b:
            is_conflict = False
            resolved = o
        else:
            is_conflict = True

        if is_conflict:
            in_conflict = True
            conflict_ours.append(o)
            conflict_theirs.append(t)
        else:
            if in_conflict:
                result_lines.append("<<<<<<< ours")
                result_lines.extend(conflict_ours)
                result_lines.append("=======")
                result_lines.extend(conflict_theirs)
                result_lines.append(">>>>>>> theirs")
                conflict_ours = []
                conflict_theirs = []
                in_conflict = False
            result_lines.append(resolved)

    if in_conflict:
        result_lines.append("<<<<<<< ours")
        result_lines.extend(conflict_ours)
        result_lines.append("=======")
        result_lines.extend(conflict_theirs)
        result_lines.append(">>>>>>> theirs")

    return "\n".join(result_lines)