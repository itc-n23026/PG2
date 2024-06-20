import sys
import openpyxl
from openpyxl import Workbook

def create_multiplication_table(n):
    # Excelワークブックとワークシートを作成
    wb = Workbook()
    ws = wb.active
    ws.title = "掛け算の表"
    
    # N x Nの掛け算表を作成
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            ws.cell(row=i, column=j, value=i * j)
    
    # ファイル名を決定
    filename = f"MultiplicationTable_{n}x{n}.xlsx"
    
    # Excelファイルに保存
    wb.save(filename)
    print(f"{filename} が作成されました。")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用方法: python script.py <数値>")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        create_multiplication_table(n)
    except ValueError:
        print("有効な整数を入力してください。")
        sys.exit(1)