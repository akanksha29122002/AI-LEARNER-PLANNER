def adjust_difficulty(level):
    if level == "beginner":
        return 0.8
    elif level == "advanced":
        return 1.2
    return 1.0
