import ezsheets

# Google Sheets APIの認証
ss = ezsheets.Spreadsheet('1KZM48hnXkXzXCVGC2CFr28YFQJgKs8F0rm3vi8oFGUM')

# 最初のシートを取得
sheet = ss[0]

# 名前とメールアドレスのリストを収集
names_and_emails = []
for row in sheet.getRows():
    if not row[1] or not row[2]:
        break
    name = row[1]
    email = row[2]
    names_and_emails.append((name, email))

# 結果を表示
for name, email in names_and_emails:
    print(f'Name: {name}, Email: {email}')