def generate_alert(predicted_load):
    alerts = []

    for load in predicted_load:
        if load >= 85:
            alerts.append("🚨 Critical Emergency Load")
        elif 60 <= load < 85:
            alerts.append("⚠ High Emergency Load")
        elif 40 <= load < 60:
            alerts.append("🔵 Moderate Load")
        else:
            alerts.append("✅ Normal Load")

    return alerts
