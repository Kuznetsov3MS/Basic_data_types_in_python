numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

numbers_length = len(numbers)
numbers_sum = sum(numbers[:4]) + sum(numbers[5:])

numbers[4] = (numbers_sum / numbers_length)

print("Измененный список:", numbers)