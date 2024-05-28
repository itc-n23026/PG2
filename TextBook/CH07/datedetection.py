import re

date_pattern = r'(?P<day>0[1-9]|[12][0-9]|3[01])/(?P<month>0[1-9]|1[0-2])/(?P<year>1[0-9]{3}|2[0-9]{3})'

print("日付を含むテキストを入力してください:")
sample_text = ""
while True:
    line = input()
    if line.strip() == "":
        break
    sample_text += line + "\n"

def is_valid_date(day, month, year):
    day = int(day)
    month = int(month)
    year = int(year)
    
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        month_days[1] = 29
    
    return 1 <= month <= 12 and 1 <= day <= month_days[month - 1]

for match in re.finditer(date_pattern, sample_text):
    day = match.group('day')
    month = match.group('month')
    year = match.group('year')
    if is_valid_date(day, month, year):
        print(f'{day}/{month}/{year} は有効な日付です。')
    else:
        print(f'{day}/{month}/{year} は有効な日付ではありません。')
