
print("---------------------Task-1--------------------------\n")

a = ["яблоко", "банан", "киви", "арбуз"]

for i in range(len(a)):
    print(str(i + 1) + ". " + '{:>10}'.format(a[i]))

print("\n-----------------------------------------------------\n")

print("---------------------Task-2--------------------------\n")

frukt = ["Апельсин", "Банан", "Картофель", "Ананас"]
ovosh = ["Помидор", "Картофель", "Морковь", "Свекла"]

for i1 in frukt:
    for i2 in ovosh:
        if i1 == i2:
            frukt.remove(i1)

print(frukt, "\n")

print("-----------------------------------------------------\n")

print("---------------------Task-3--------------------------\n")

spisok1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
spisok2 = []

for i in range(len(spisok1)):
    if (spisok1[i] % 2) == 0:
        spisok2.insert(i, (spisok1[i] * 2))
    else:
        spisok2.insert(i, (spisok1[i] / 4))

print(spisok2, "\n")


print("-----------------------------------------------------\n")