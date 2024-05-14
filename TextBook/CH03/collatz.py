def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

while True:
    try:
        number = int(input("数値を入力してください: "))
        break
    except ValueError:
        print("無効な入力です。整数を入力してください。")

print(number)

while number != 1:
    number = collatz(number)
    print(number)