"""МКР OPI. Завдання 09: Вибір моделі життєвого циклу."""


def recommend_model(project: dict) -> str:
    if not isinstance(project, dict):
        raise ValueError("Некоректний проект: project")

    required_int_keys = ["stability", "risk", "feedback"]
    for key in required_int_keys:
        if (
            key not in project
            or not isinstance(project[key], int)
            or isinstance(project[key], bool)
            or not (1 <= project[key] <= 5)
        ):
            raise ValueError(f"Некоректний проект: {key}")

    if "regulated" not in project or not isinstance(project["regulated"], bool):
        raise ValueError("Некоректний проект: regulated")

    models_data = [
        ("Каскад", (5, 1, 1)),
        ("V-модель", (4, 2, 1)),
        ("Спіральна", (2, 5, 3)),
        ("Прототипування", (1, 3, 5)),
    ]
    weights = (3, 2, 2)

    stability = project["stability"]
    regulated = project["regulated"]

    filtered_out = []
    active_models = []

    for name, ideals in models_data:
        reason = None
        if stability <= 2 and name in ("Каскад", "V-модель"):
            reason = "низька стабільність вимог"
        elif regulated and name == "Прототипування":
            reason = "регульований проєкт"

        if reason:
            filtered_out.append(f"{name} ({reason})")
        else:
            p_vals = (project["stability"], project["risk"], project["feedback"])
            score = sum(w * (4 - abs(p - i)) for w, p, i in zip(weights, p_vals, ideals))
            active_models.append((name, score))

    lines = []
    if filtered_out:
        lines.append(f"Відсічено: {'; '.join(filtered_out)}")
    else:
        lines.append("Відсічено: немає")

    ranked = sorted(active_models, key=lambda x: x[1], reverse=True)

    for i, (name, score) in enumerate(ranked, start=1):
        lines.append(f"{i}. {name} — {score}")

    if len(ranked) >= 2 and ranked[0][1] == ranked[1][1]:
        lines.append(f"Рекомендація: потрібне обговорення ({ranked[0][0]}, {ranked[1][0]})")
    elif ranked:
        lines.append(f"Рекомендація: {ranked[0][0]}")

    return "\n".join(lines)