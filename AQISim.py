wind_speed_input = int(input("Enter the wind speed(km/h): "))
factory_emission_level_input = int(input("Enter the factory emmision level(0~10): "))
traffic_volume_input = input("Enter traffic volume(high or medium): ").lower()
raining_input = input("Is it raining?(y/n):　").lower() == "y"
number_of_simulation_days_input = int(input("number of simulation days: "))


def simulate_pm25(wind_speed_input, factory_emission_level_input,
                  traffic_volume_input, raining_input,
                  number_of_simulation_days_input):
    pm25 = 50
    record = []
    for day in range(1, number_of_simulation_days_input + 1):
        change = 0
        #change是pm25的變化量
        
        if wind_speed_input > 15:
            change -= 10
        elif wind_speed_input < 5:
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

        pm25 = max(0, pm25 + change)
              #確保低於0時，會顯示0不會顯示負數
        
        record.append((day, pm25))

    return record


result = simulate_pm25(wind_speed_input,
                      factory_emission_level_input,
                      traffic_volume_input, raining_input,
                      number_of_simulation_days_input)
print("simulation result: ")

try:
    
    with open("result.txt", "w", encoding="utf-8") as file:
        #用a不是w的話，就會變成每筆資料新增在前一筆後面(append)
        for day, value in result:
            #result(day,pm25)
            if value > 80:
                line = f"⚠️ Day {day}: PM2.5 = {value} μg/m³ → Unhealthy\n"
            else:
                line = f"Day {day}: PM2.5 = {value} μg/m³\n"

            print(line)
            file.write(line)
except Exception as e:
    print("Error", e)

input("\npress Enter to leave")
