def build_relationships(events):

    chain = []

    for event in events:

        event_type = event.event_type.lower()

        if "audit" in event_type:
            chain.append(
                "Audit Finding Detected"
            )

        elif "remediation" in event_type:
            chain.append(
                "Remediation Assigned"
            )

        elif "deadline" in event_type:
            chain.append(
                "Remediation Failed"
            )

        elif "regulation" in event_type:
            chain.append(
                "Risk Increased Due To New Regulation"
            )

    return {
        "relationships": chain
    }