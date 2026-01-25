salary = 5000
initial_spend = 6000
increase = 0.03
months = 10

# асчёт подушки безопаности
money_capital = 0
for i in range(months):
    spend = initial_spend + i * increase
    balance = salary - spend
    money_capital -= balance  # необходимая подушка безопасности

print(f"Необходимая подушка безопасности: {money_capital:.2f}")