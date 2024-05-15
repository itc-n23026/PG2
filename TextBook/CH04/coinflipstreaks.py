import random

number_of_streaks = 0

for experiment_number in range(10000):
    coin_flips = [random.choice(['H', 'T']) for _ in range(100)]

    streak = 1
    for i in range(1, 100):
        if coin_flips[i] == coin_flips[i - 1]:
            streak += 1
            if streak == 6:
                number_of_streaks += 1
                break
        else:
            streak = 1

print(f'同じ面が6連続出現する確率: {number_of_streaks / 100:.2f}%')