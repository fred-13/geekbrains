#---------------------Task-1--------------------------

a = input("Введите любое число от 0 до 10: ")
while True:
    if int(a) > 0 and int(a) < 10:
        print("Возведем ваще число в степень 2 и получим: " + str(int(a) ** 2))
        break
    else:
        a = input("Вы ввели неверное число. Попробуйте еще раз: ")
        continue

#-----------------------------------------------------

#---------------------Task-2--------------------------

b = input("Введите число B: ")
c = input("Введите число C: ")
b, c = c, b
print("Мы переопределили твои переменные и теперь B = " + str(b) + " а C = " + str(c))

#-----------------------------------------------------
