while True:
    start_km = float(input("Введите начальный результат пробега в км : "))
    target_km = float(input("Введите желаемый результат пробега в км : "))
    days = 1
    if start_km <= 0 or target_km <= 0:
        print("Начальный и желаемый результат должен быть больше нуля! Введите ещё раз! ")
    else:
        while start_km < target_km:
            start_km *= 1.1
            days += 1
        print(f"Вы добьетесь желаемого результата за : {days} дней")
        break