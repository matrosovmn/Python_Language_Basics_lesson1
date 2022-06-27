true_password = 'qwerty'
try_count = 3
current_try = 1
success = False

while current_try <= try_count and not success:
    user_password = input('Введите пароль - ')

    if user_password == true_password:
        success = True
        print('Пароль верный, доступ разрешен')
    else:
        print('Пароль неверный, осталось попыток', try_count - current_try)
        current_try = current_try + 1

    if current_try > try_count:
        print('Все попытки исчерпаны!\nДоступ запрещен!')
