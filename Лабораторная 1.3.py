
players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# Определяем середину списка
middle = len(players) // 2

# Создаем первую команду (первые три игрока)
team1 = []
for i in range(middle):
    team1.append(players[i])

# Создаем вторую команду (последние три игрока)
team2 = []
for i in range(middle, len(players)):
    team2.append(players[i])

# Выводим результаты
print("Команда 1:")
for player in team1:
    print(player)

print("\nКоманда 2:")
for player in team2:
    print(player)