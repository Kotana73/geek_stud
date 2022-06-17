# Пользователь вводит время в секунды конвертируем их в часы и минуты.
sec = int(input('вводим время в секундах : '))
sec_value = sec % (24 * 3600)
hour_value = sec_value // 3600
sec_value %= 3600
min_value = sec_value // 60
sec_value %= 60
<<<<<<< HEAD
print("конвертация секунд в часах с минутами:", f'{hour_value:02d}:{min_value:02d}:{sec_value:02d}')
=======
print("конвертация секунд в часах с минутами:", hour_value,":", min_value, ":", sec_value)
>>>>>>> origin/stud_geek_lesson1
