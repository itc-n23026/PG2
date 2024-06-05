import random

guess = ''
while guess not in ('表', '裏'):
    print('コインの裏表を当ててください。裏か表を入力してください:')
    guess = input()

toss = '表' if random.randint(0, 1) == 0 else '裏' # tossの値を'裏'か'表'に変換する

if toss == guess:
    print('当たり！')
else:
    print('はずれ！もう一回当てて！')
    guess = input()
    
    toss = '表' if random.randint(0, 1) == 0 else '裏' # はずれの場合、再度  トスを行う

    if toss == guess:
        print('当たり！')
    else:
        print('はずれ。このゲームは苦手ですね。')