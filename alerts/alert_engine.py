def generate_alert(predicted_load):
    alerts = []

    for load in predicted_load:
        if load > 80:
            alerts.append("High Emergency Load 🚨")
        elif load > 50:
            alerts.append("Moderate Emergency Load ⚠")
        else:
            alerts.append("Normal Load ✅")

    return alerts
