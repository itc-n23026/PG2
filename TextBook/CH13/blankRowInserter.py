import sys
import openpyxl
from openpyxl.utils import range_boundaries

def insert_empty_rows(n, m, filename):
    try:
        # Excelファイルを開く
        wb = openpyxl.load_workbook(filename)
    except openpyxl.utils.exceptions.InvalidFileException:
        print(f"エラー: {filename} は有効なExcelファイルではありません。")
        sys.exit(1)
    except FileNotFoundError:
        print(f"エラー: ファイル {filename} が見つかりません。")
        sys.exit(1)
    except Exception as e:
        print(f"予期しないエラーが発生しました: {e}")
        sys.exit(1)

    ws = wb.active
    
    # N行目のところにM行の空行を挿入
    ws.insert_rows(n, amount=m)
    
    # ファイルを保存
    wb.save(filename)
    print(f"{filename} の {n} 行目に {m} 行の空行を挿入しました。")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("使用方法: python3 blankRowInserter.py <N> <M> <ファイル名>")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        filename = sys.argv[3]
        insert_empty_rows(n, m, filename)
    except ValueError:
        print("有効な整数を入力してください。")
        sys.exit(1)
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        sys.exit(1)