SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR  = 3600

time = int(input("Введите время в секундах: "))

hours = time // SECONDS_IN_HOUR
minutes = (time // SECONDS_IN_MINUTE) - (hours * SECONDS_IN_MINUTE)
seconds = time % SECONDS_IN_MINUTE

print(f"{hours:02}:{minutes:02}:{seconds:02}")


