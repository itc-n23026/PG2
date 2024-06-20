import sys
import openpyxl

def insert_texts_to_sheet(filenames, output_filename):
    # 新しいワークブックとワークシートを作成
    wb = openpyxl.Workbook()
    ws = wb.active
    
    for col_idx, filename in enumerate(filenames, start=1):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for row_idx, line in enumerate(lines, start=1):
                    ws.cell(row=row_idx, column=col_idx, value=line.strip())
        except FileNotFoundError:
            print(f"エラー: ファイル {filename} が見つかりません。")
        except Exception as e:
            print(f"ファイル {filename} の読み込み中にエラーが発生しました: {e}")
    
    # 新しいファイルに保存
    wb.save(output_filename)
    print(f"{output_filename} が作成されました。")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("使用方法: python3 txt2xlsx.py <出力ファイル名> <入力ファイル1> <入力ファイル2> ...")
        sys.exit(1)
    
    output_filename = sys.argv[1]
    input_filenames = sys.argv[2:]
    
    insert_texts_to_sheet(input_filenames, output_filename)