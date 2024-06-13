#! python3
# searchpypi.py
import requests, sys, webbrowser, bs4

print('Searching...')
res = requests.get('http://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# 上位の検索結果のリンクを取得する
soup = bs4.BeautifulSoup(res.text, 'html.parser')
link_elems = soup.select('.package-snippet')

# 各結果をブラウザのタブで開く
num_open = min(5, len(link_elems))
for i in range(num_open):
    url_to_open = 'https://pypi.org' + link_elems[i].get('href')
    print('Opening', url_to_open)
    webbrowser.open(url_to_open)