
print("---------------------Task-1--------------------------\n")

spisok = [0, 1, 2, 3, 4, 5]
print([i**2 for i in spisok])

print("\n-----------------------------------------------------\n")

print("---------------------Task-2--------------------------\n")

frukty1 = ["Ананас", "Банан", "Апельсин", "Лимон"]
frukty2 = ["Лимон", "Грейпфрут", "Банан", "Киви"]
print([f1 for f1 in frukty1 for f2 in frukty2 if f1 == f2])

print("\n-----------------------------------------------------\n")


print("---------------------Task-3--------------------------\n")

spisok_chisel = [24, 30, -23, 10, 56, -30, 22, 15, -15]
print([a for a in spisok_chisel if a > 0 if a % 4 != 0 if a % 3 == 0])

print("\n-----------------------------------------------------\n")