numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# Ищем позицию None
for i in range(len(numbers)):
    if numbers[i] is None:
        # Вычисляем среднее соседних значений
        numbers[i] = (numbers[i-1] + numbers[i+1]) / 2
        break

print("Измененный список:", numbers)
