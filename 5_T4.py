Cities = []
credits = 5
for credit in range(credits):
    CityInput = input(f"enter city name ({credits - credit} credits left): ")
    Cities.append(CityInput)
for city in Cities:
    print(city)