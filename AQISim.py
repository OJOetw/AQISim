wind_speed_input = int(input("Enter the wind speed(km/h): "))
factory_emission_level_input = int(input("Enter the factory emmision level(0~10): "))
traffic_volume_input = int(input("Enter traffic volume: "))
raining_input = int(input("Is it raining?(y/n):　"))
number_of_simulation_days_input = int(input("number of simulation days' "))


def simulate_pm25(wind_speed_input, factory_emission_level_input, tracffic_volume, raining_input, number_of_simularion_days_input):
    pm25 = 50
    record = []

    for day in range(1, days + 1):
        






