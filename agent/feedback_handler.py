from agent.memory import save_user_feedback

def update_plan_with_feedback(data: dict):
    user_id = data.get("user_id", "default_user")
    feedback = data["feedback"]

    save_user_feedback(user_id, feedback)

    return {
        "message": "Feedback received. Future plans will be adjusted.",
        "feedback": feedback
    }
