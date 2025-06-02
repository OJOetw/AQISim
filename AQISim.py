wind_speed_input = int(input("Enter the wind speed(km/h): "))
factory_emission_level_input = int(input("Enter the factory emmision level(0~10): "))
traffic_volume_input = int(input("Enter traffic volume: "))
raining_input = input("Is it raining?(y/n):　")
number_of_simulation_days_input = int(input("number of simulation days: "))


def simulate_pm25(wind_speed_input, factory_emission_level_input, tracffic_volume_input, raining_input, number_of_simulation_days_input):
    pm25 = 50
    record = []

    for day in range(1, number_of_simulation_days_input + 1):
        change = 0

        if wind_speed_input > 15:
            change -= 10
        elif windZ_speed_input < 5:
            change += 5

        change += factory_emission_level_input * 2


        if traffic_volume_input == "high":
            change += 7
        elif traffic_volume_input == "medium":
            change += 4
        else:
            change += 1

        if raining_input:
            change -= 8


        pm25 = max(0. pm25 + change)
        record.append(day, pm25)





