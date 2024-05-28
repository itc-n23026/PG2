import re

def custom_strip(s: str, chars: str = None) -> str:
    if chars is None:
        pattern = r'^\s+|\s+$'
    else:
        escaped_chars = re.escape(chars)
        pattern = f'^[{escaped_chars}]+|[{escaped_chars}]+$'

    return re.sub(pattern, '', s)

def user_input_strip():
    s = input("文字列を入力してください: ")
    chars = input("除去する文字を入力してください（入力がない場合、空白を除去します）: ")
    if chars == "":
        chars = None

    stripped = custom_strip(s, chars)
    if chars is None:
        print(f"元の文字列: '{s}' | 除去後: '{stripped}'")
    else:
        print(f"元の文字列: '{s}' 除去する文字: '{chars}' | 除去後: '{stripped}'")

user_input_strip()
