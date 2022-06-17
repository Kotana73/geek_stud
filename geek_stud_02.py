# Пользователь вводит время в секунды конвертируем их в часы и минуты.
sec = int(input('вводим время в секундах : '))
sec_value = sec % (24 * 3600)
hour_value = sec_value // 3600
sec_value %= 3600
min_value = sec_value // 60
sec_value %= 60
print("конвертация секунд в часах с минутами:", hour_value,":", min_value, ":", sec_value)