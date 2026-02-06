from agent.scheduler import build_schedule
from agent.evaluator import evaluate_plan

def generate_learning_plan(user_input: dict):
    goal = user_input["goal"]
    days = user_input["days"]
    hours_per_day = user_input["hours_per_day"]
    level = user_input["level"]

    modules = [
        "Basics",
        "Core Concepts",
        "Intermediate Topics",
        "Projects",
        "Revision"
    ]

    schedule = build_schedule(modules, days, hours_per_day)
    evaluation = evaluate_plan(schedule)

    return {
        "goal": goal,
        "modules": modules,
        "schedule": schedule,
        "evaluation": evaluation
    }
