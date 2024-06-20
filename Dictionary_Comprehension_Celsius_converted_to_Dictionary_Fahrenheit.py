
# weather_c = eval(input())
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}


print(f"weather in C: {weather_c}")

# new_dict = {new_key: new_value for (key, value) in dict.item() if testpasses}
weather_f = {day: (temp*(9 / 5) + 32) for (day, temp) in weather_c.items()}
print(f"weather in F: {weather_f}")


# print(f"Celcius temp is: {monday.temp}")

# Fahrenheit_conversion = monday.temp*(9 / 5) + 32

# print(f"Fahrenheit temp is: {Fahrenheit_conversion}")

# print(weather_f)
