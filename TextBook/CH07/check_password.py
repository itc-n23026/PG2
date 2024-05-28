import re

def is_strong_password(password):
    if len(password) < 8:
        return password, False

    if not re.search(r'[A-Z]', password):
        return password, False
    
    if not re.search(r'[a-z]', password):
        return password, False
    
    if not re.search(r'[0-9]', password):
        return password, False
    
    return password, True

user_password = input("パスワードを入力してください: ")

password, is_strong = is_strong_password(user_password)

if is_strong:
    print(f"{password} は強力なパスワードです。")
else:
    print(f"{password} は強力なパスワードではありません。")
