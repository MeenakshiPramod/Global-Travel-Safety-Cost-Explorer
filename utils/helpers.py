def generate_travel_advice(weather_data, air_quality_data):

    advice = []

    # Weather Advice
    if weather_data:

        temp = weather_data["temp"]

        if temp < 10:
            advice.append(
                "Cold weather expected. Carry warm clothes."
            )

        elif temp > 32:
            advice.append(
                "Very hot weather. Stay hydrated."
            )

        else:
            advice.append(
                "Weather conditions look pleasant for travel."
            )

    # Air Quality Advice
    if air_quality_data:

        aqi = air_quality_data["aqi"]

        if aqi >= 4:
            advice.append(
                "Poor air quality detected. Consider wearing a mask."
            )

        elif aqi == 3:
            advice.append(
                "Moderate air quality."
            )

        else:
            advice.append(
                "Air quality is good."
            )

    # Default Advice
    if not advice:
        return "Travel information unavailable currently."

    return " ".join(advice)