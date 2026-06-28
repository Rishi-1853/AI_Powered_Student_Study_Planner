def detect_weak_subjects(subject_scores):

    weak_subjects = []

    for subject, score in subject_scores.items():

        if score < 60:

            weak_subjects.append(subject)

    return weak_subjects


def generate_daily_goals(weak_subjects):

    goals = []

    for subject in weak_subjects:

        goals.append(
            f"Spend 2 hours on {subject}"
        )

        goals.append(
            f"Revise important concepts of {subject}"
        )

        goals.append(
            f"Solve 10 practice questions in {subject}"
        )

    return goals


def generate_recommendations(student):

    recommendations = []

    if student["study_hours"] < 4:

        recommendations.append(
            "Increase study hours to at least 4 hours daily."
        )

    if student["attendance"] < 75:

        recommendations.append(
            "Improve attendance to above 75%."
        )

    if student["stress_level"] > 7:

        recommendations.append(
            "Take short breaks and manage stress."
        )

    if student["motivation"] < 5:

        recommendations.append(
            "Set small daily goals."
        )

    return recommendations


def performance_tips(score):

    if score >= 85:

        return [
            "Maintain current routine",
            "Attempt more mock tests"
        ]

    elif score >= 70:

        return [
            "Increase revision frequency",
            "Practice previous year questions"
        ]

    else:

        return [
            "Increase study hours",
            "Focus on weak subjects",
            "Improve attendance"
        ]


def analyze_student(
    student,
    subject_scores
):

    weak_subjects = sorted(
    subject_scores,
    key=subject_scores.get
    )[:3]

    goals = generate_daily_goals(
        weak_subjects
    )

    recommendations = generate_recommendations(
        student
    )

    tips = performance_tips(
        student["predicted_score"]
    )

    return {

        "weak_subjects": weak_subjects,

        "daily_goals": goals,

        "recommendations": recommendations,

        "tips": tips
    }