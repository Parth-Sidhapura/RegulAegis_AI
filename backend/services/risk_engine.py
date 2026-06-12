def calculate_risk(events):

    if not events:
        return {
            "score": 0,
            "level": "Low",
            "reasons": []
        }

    total_score = 0
    reasons = []

    for event in events:

        event_score = 0

        severity = str(event.severity).lower()
        status = str(event.status).lower()
        event_type = str(event.event_type).lower()

        # Severity

        if severity == "critical":
            event_score += 40

        elif severity == "high":
            event_score += 25

        elif severity == "medium":
            event_score += 15

        elif severity == "low":
            event_score += 5

        # Status

        if status == "open":
            event_score += 10

        elif status == "pending":
            event_score += 5

        elif status == "closed":
            event_score -= 5

        # Event Type

        if "audit" in event_type:
            event_score += 10
            reasons.append("Audit finding detected")

        if "deadline" in event_type:
            event_score += 15
            reasons.append("Missed deadline detected")

        if "regulation" in event_type:
            event_score += 10
            reasons.append("Regulation impact detected")

        total_score += event_score

    # IMPORTANT
    score = int(total_score / len(events))

    if score >= 80:
        level = "Critical"

    elif score >= 60:
        level = "High"

    elif score >= 30:
        level = "Medium"

    else:
        level = "Low"

    return {
        "score": score,
        "level": level,
        "reasons": list(set(reasons))
    }