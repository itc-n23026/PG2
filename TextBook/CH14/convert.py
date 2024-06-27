import sys
import ezsheets

def convert_and_download(file_path):
    # Google Sheets APIの認証
    ss = ezsheets.upload(file_path)

    # ファイル名から拡張子を取得して、他の形式に変換してダウンロード
    base_name = file_path.split('.')[0]  # 拡張子を除いたファイル名
    ss.downloadAsExcel(f'{base_name}.xlsx')
    ss.downloadAsODS(f'{base_name}.ods')
    ss.downloadAsCSV(f'{base_name}.csv')
    ss.downloadAsPDF(f'{base_name}.pdf')
    ss.downloadAsHTML(f'{base_name}.html')

    print('ファイルの変換とダウンロードが完了しました。')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python script_name.py file_path')
    else:
        file_path = sys.argv[1]
        convert_and_download(file_path)