def generate_alert(predicted_value):

    if predicted_value > 35:
        return "HIGH EMERGENCY PRESSURE"
    elif predicted_value > 20:
        return "MODERATE PRESSURE"
    else:
        return "NORMAL"
