from datetime import datetime, date


# ==========================================
# CALCULATE DAYS LEFT UNTIL EXAM
# ==========================================

def days_until_exam(exam_date):
    """
    exam_date format: YYYY-MM-DD

    Example:
    2026-07-15
    """

    today = date.today()

    exam_date = datetime.strptime(
        exam_date,
        "%Y-%m-%d"
    ).date()

    days_left = (exam_date - today).days

    return max(days_left, 0)


# ==========================================
# CALCULATE PRIORITY BASED ON DAYS LEFT
# ==========================================

def calculate_priority(days_left):

    if days_left <= 3:
        return "High"

    elif days_left <= 10:
        return "Medium"

    else:
        return "Low"


# ==========================================
# CALCULATE URGENCY SCORE
# ==========================================

def calculate_urgency(days_left):

    if days_left <= 0:
        return 10

    urgency = 30 / (days_left + 1)

    return round(min(urgency, 10), 2)


# ==========================================
# CALCULATE PRIORITY SCORE
# ==========================================

def calculate_priority_score(
    difficulty,
    days_left
):
    """
    difficulty = 1-10

    Higher score means
    higher study priority
    """

    urgency = calculate_urgency(
        days_left
    )

    score = (

        difficulty * 0.7

        +

        urgency * 0.3

    )

    return round(score, 2)


# ==========================================
# ASSIGN PRIORITY USING SCORE
# ==========================================

def score_to_priority(score):

    if score >= 8:
        return "High"

    elif score >= 5:
        return "Medium"

    else:
        return "Low"


# ==========================================
# CALCULATE SUBJECT WEIGHTS
# ==========================================

def calculate_weight(priority):

    weights = {

        "High": 3,

        "Medium": 2,

        "Low": 1
    }

    return weights.get(
        priority,
        1
    )


# ==========================================
# ALLOCATE STUDY HOURS
# ==========================================

def allocate_hours(
    priorities,
    total_hours
):

    weights = [

        calculate_weight(p)

        for p in priorities
    ]

    total_weight = sum(weights)

    allocated = []

    for weight in weights:

        hours = round(

            (
                weight
                /
                total_weight
            )

            * total_hours,

            2
        )

        allocated.append(hours)

    return allocated


# ==========================================
# GENERATE TIME SLOTS
# ==========================================

def generate_time_slots(
    start_hour,
    study_hours
):

    slots = []

    current = start_hour

    for hrs in study_hours:

        end_time = current + hrs

        slots.append(

            f"{current:.2f} - {end_time:.2f}"

        )

        current = end_time

    return slots


# ==========================================
# CREATE FULL STUDY PLAN
# ==========================================

def create_study_plan(
    subjects,
    difficulties,
    exam_dates,
    available_hours
):

    days_left = [

        days_until_exam(date)

        for date in exam_dates
    ]

    scores = [

        calculate_priority_score(
            difficulty,
            days
        )

        for difficulty, days

        in zip(
            difficulties,
            days_left
        )
    ]

    priorities = [

        score_to_priority(score)

        for score in scores
    ]

    allocated_hours = allocate_hours(

        priorities,

        available_hours
    )

    plan = []

    for subject, priority, hours, score in zip(

        subjects,

        priorities,

        allocated_hours,

        scores
    ):

        plan.append({

            "subject": subject,

            "priority": priority,

            "priority_score": score,

            "allocated_hours": hours
        })

    return plan


# ==========================================
# TESTING
# ==========================================

if __name__ == "__main__":

    subjects = [

        "Math",

        "Physics",

        "Programming"
    ]

    difficulties = [

        9,

        7,

        5
    ]

    exam_dates = [

        "2026-06-20",

        "2026-06-25",

        "2026-07-10"
    ]

    available_hours = 6

    plan = create_study_plan(

        subjects,

        difficulties,

        exam_dates,

        available_hours
    )

    print("\nSTUDY PLAN\n")

    for item in plan:

        print(item)

