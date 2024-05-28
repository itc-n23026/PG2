import pyinputplus as pyip

bread = pyip.inputMenu(['小麦パン', '白パン', 'サワー種'], prompt='パンの種類を選んでください:\n', numbered=True)

protein = pyip.inputMenu(['チキン', 'ターキー', 'ハム', '豆腐'], prompt='タンパク質の種類を選んでください:\n', numbered=True)

cheese_needed = pyip.inputYesNo('チーズは必要ですか？ (はい/いいえ): ', yesVal='はい', noVal='いいえ')
if cheese_needed == 'はい':
    cheese = pyip.inputMenu(['チェダー', 'スイス', 'モッツァレラ'], prompt='チーズの種類を選んでください:\n', numbered=True)
else:
    cheese = 'なし'

mayo_needed = pyip.inputYesNo('マヨネーズは必要ですか？ (はい/いいえ): ', yesVal='はい', noVal='いいえ')

mustard_needed = pyip.inputYesNo('からしは必要ですか？ (はい/いいえ): ', yesVal='はい', noVal='いいえ')

lettuce_needed = pyip.inputYesNo('レタスは必要ですか？ (はい/いいえ): ', yesVal='はい', noVal='いいえ')

tomato_needed = pyip.inputYesNo('トマトは必要ですか？ (はい/いいえ): ', yesVal='はい', noVal='いいえ')

number_of_sandwiches = pyip.inputInt('サンドイッチはいくつ欲しいですか？ ', min=1)

print(f'\nあなたのサンドイッチの注文内容:')
print(f'パンの種類: {bread}')
print(f'タンパク質の種類: {protein}')
print(f'チーズ: {cheese}')
print(f'マヨネーズ: {"あり" if mayo_needed == "はい" else "なし"}')
print(f'からし: {"あり" if mustard_needed == "はい" else "なし"}')
print(f'レタス: {"あり" if lettuce_needed == "はい" else "なし"}')
print(f'トマト: {"あり" if tomato_needed == "はい" else "なし"}')
print(f'サンドイッチの数: {number_of_sandwiches}')
