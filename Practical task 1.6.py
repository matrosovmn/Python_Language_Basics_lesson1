revenue = int(input("Введите  выручку : "))
costs = int(input("Введите  издержки : "))

if revenue - costs > 0:
    print("Фирма работает с прибылью :", (revenue - costs))
    print(f"Рентабельность выручки составляет: {( revenue - costs) / revenue:.2f}")
    person = int(input("Сколько сотрудников работает в фирме? : "))
    print(f"Прибыль на одного работника составляет: {(revenue - costs) / person:.2f}")
elif revenue - costs < 0:
    print(f"Фирма работает с убытком : {(revenue - costs)}")
else:
    print(f"Фирма работает в ноль : {(revenue - costs)}")
