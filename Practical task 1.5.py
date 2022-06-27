revenue = int(input("Введите  прибыль : "))
costs = int(input("Введите  издержки : "))

if revenue - costs > 0:
    print("Фирма работает с прибылью :", (revenue - costs))
elif revenue - costs < 0:
    print(f"Фирма работает с убытком : {(revenue - costs)}")
else:
    print(f"Фирма работает в ноль : {(revenue - costs)}")
