"""МКР OPI. Завдання 01: Ознаки кризи проєкту."""


def crisis_signs(
    plan_cost: int,
    fact_cost: int,
    plan_weeks: int,
    fact_weeks: int,
    delivered: int,
    total: int,
) -> str:
    args = [plan_cost, fact_cost, plan_weeks, fact_weeks, delivered, total]
    for arg in args:
        if not isinstance(arg, int) or isinstance(arg, bool):
            raise ValueError("Некоректні дані")

    if (
        plan_cost <= 0
        or fact_cost <= 0
        or plan_weeks <= 0
        or fact_weeks <= 0
        or total <= 0
        or not (0 <= delivered <= total)
    ):
        raise ValueError("Некоректні дані")

    signs = []
    if fact_cost * 5 > plan_cost * 6:
        signs.append("Перевищено бюджет")
    if fact_weeks * 5 > plan_weeks * 6:
        signs.append("Зірвано строки")
    if delivered * 4 < total * 3:
        signs.append("Недопоставлено функції")

    count = len(signs)
    line1 = f"Ознак кризи: {count}"
    line2 = f"Ознаки: {'; '.join(signs)}" if signs else "Ознаки: немає"

    if count == 0:
        line3 = "Висновок: проєкт у нормі"
    elif count == 1:
        line3 = "Висновок: є ризик кризи"
    else:
        line3 = "Висновок: криза проєкту"

    return f"{line1}\n{line2}\n{line3}"