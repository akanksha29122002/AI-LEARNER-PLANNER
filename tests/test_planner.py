from agent.planner import generate_learning_plan

def test_generate_plan():
    sample_input = {
        "goal": "Learn Machine Learning",
        "days": 10,
        "hours_per_day": 2,
        "level": "beginner"
    }

    result = generate_learning_plan(sample_input)
    assert "schedule" in result
    assert len(result["schedule"]) > 0
