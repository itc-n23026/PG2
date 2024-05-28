import random
import time

def multiplication_quiz():
    num_questions = 10
    max_attempts = 3
    timeout = 8
    score = 0

    for _ in range(num_questions):
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        correct_answer = a * b
        attempts = 0
        answered_correctly = False

        while attempts < max_attempts and not answered_correctly:
            start_time = time.time()
            try:
                answer = int(input(f"問題: {a} x {b} = "))
                response_time = time.time() - start_time

                if response_time > timeout:
                    print("時間切れ！次の問題に移ります。")
                    break

                if answer == correct_answer:
                    print("正解！")
                    answered_correctly = True
                    score += 1
                    time.sleep(1)
                else:
                    print("不正解！")
                attempts += 1

            except ValueError:
                print("数値を入力してください。")

        if not answered_correctly:
            print(f"正解は {correct_answer} でした。")
            time.sleep(1)

    print(f"スコア: {score} / {num_questions}")

if __name__ == "__main__":
    multiplication_quiz()
