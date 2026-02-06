def evaluate_plan(schedule):
    if len(schedule) == 0:
        return "Plan is empty ❌"

    if len(schedule) < 5:
        return "Plan may be too short ⚠️"

    return "Plan looks feasible ✅"
