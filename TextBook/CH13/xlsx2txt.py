import sys
import openpyxl

def export_columns_to_files(input_filename, output_prefix):
    # Excelファイルを開く
    wb = openpyxl.load_workbook(input_filename)
    ws = wb.active
    
    # 列ごとに内容をテキストファイルに書き込む
    for col_idx, col in enumerate(ws.iter_cols(values_only=True), start=1):
        output_filename = f"{output_prefix}_col{col_idx}.txt"
        try:
            with open(output_filename, 'w', encoding='utf-8') as file:
                for cell in col:
                    if cell is not None:
                        file.write(f"{cell}\n")
            print(f"{output_filename} が作成されました。")
        except Exception as e:
            print(f"ファイル {output_filename} の書き込み中にエラーが発生しました: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("使用方法: python3 xlsx2txt.py <入力ファイル名> <出力ファイルプレフィックス>")
        sys.exit(1)
    
    input_filename = sys.argv[1]
    output_prefix = sys.argv[2]
    
    export_columns_to_files(input_filename, output_prefix)