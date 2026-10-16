numbers = [12, 45, 7, 89, 23, 56, 14, 91, 38, 62]

print("Массив чисел:", numbers)

max_number = numbers[0]

for number in numbers:
    if number > max_number:
        max_number = number

print("Наибольшее число:", max_number)
