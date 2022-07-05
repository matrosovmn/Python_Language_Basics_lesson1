# name = input("Введите имя :")
# surname = input("Введите фамилию :")
# year = input("Введите год рождения :")
# city = input("Введите город проживания :")
# email = input("Введите email :")
# telephone = input("Введите телефон :")


def personal(name, surname, year, city, email, telephone):
    return ' '.join(["имя: ", name,
                     "фамилия: ", surname,
                     "год рождения: ", year,
                     "город проживания: ", city,
                     "email: ", email,
                     "телефон: ", telephone])

# print(personal(name=name, surname=surname, year=year, city=city, email=email, telephone=telephone))

params = {
"name": input("Введите имя :"),
"surname": input("Введите фамилию :"),
"year": input("Введите год рождения :"),
"city": input("Введите город проживания :"),
"email": input("Введите email :"),
"telephone": input("Введите телефон :"),
}

# Оператор ** соберёт все переданные именованные аргументы в словарь - очень круто!!!
print(personal(**params))
