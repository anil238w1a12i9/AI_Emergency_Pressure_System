def generate_alert(predicted_load):
    alerts = []
    for load in predicted_load:
        if load > 35:
            alerts.append("HIGH EMERGENCY PRESSURE")
        elif load > 20:
            alerts.append("MODERATE PRESSURE")
        else:
            alerts.append("NORMAL")
    return alerts
