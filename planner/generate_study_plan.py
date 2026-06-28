def generate_study_plan(subjects, priorities, total_hours):

    weights = {
        "High": 3,
        "Medium": 2,
        "Low": 1
    }

    total_weight = sum(
        weights[p]
        for p in priorities
    )

    schedule = []

    for subject, priority in zip(
        subjects,
        priorities
    ):

        allocated_hours = round(
            (
                weights[priority]
                / total_weight
            ) * total_hours,
            2
        )

        schedule.append({

            "subject": subject,
            "priority": priority,
            "hours": allocated_hours
        })

    return schedule


# Example

subjects = [
    "Math",
    "Physics",
    "Programming"
]

priorities = [
    "High",
    "Medium",
    "Low"
]

available_hours = 6

plan = generate_study_plan(
    subjects,
    priorities,
    available_hours
)

for item in plan:

    print(
        f"{item['subject']} "
        f"({item['priority']}) "
        f"→ {item['hours']} hrs"
    )