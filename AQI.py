def compute_air_quality(pm25, pm10, no2, co):

    aqi_value = (pm25 + pm10 + no2 + (co * 50)) / 4

    if aqi_value <= 50:
        status = "Clean Air"
    elif aqi_value <= 100:
        status = "Acceptable"
    elif aqi_value <= 150:
        status = "Sensitive Groups Risk"
    elif aqi_value <= 200:
        status = "Poor"
    else:
        status = "Very Dangerous"

    return aqi_value, status


def air_quality_agent():

    print("----- Air Quality Monitoring Agent -----")

    try:
        pm25 = float(input("Enter PM2.5 value: "))
        pm10 = float(input("Enter PM10 value: "))
        no2 = float(input("Enter NO2 value: "))
        co = float(input("Enter CO value: "))

        aqi, condition = compute_air_quality(pm25, pm10, no2, co)

        print("\nCalculated AQI:", round(aqi, 2))
        print("Air Quality Condition:", condition)

    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    air_quality_agent()
