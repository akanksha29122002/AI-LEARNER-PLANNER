def build_schedule(modules, total_days, hours_per_day):
    schedule = []
    day = 1

    for module in modules:
        schedule.append({
            "day": day,
            "topic": module,
            "duration_hours": hours_per_day
        })
        day += 1
        if day > total_days:
            break

    return schedule
