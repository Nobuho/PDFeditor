import img2pdf
import os
from glob import glob

# 各画像を格納したフォルダの直下に、画像があるようにすること
# PDFのファイル名はフォルダ名になる

# 画像を格納したフォルダの親フォルダ
path = "C:\\_Python\\PDFeditor\\img"
# 画像の拡張子 *pngはダメらいしい？未検証
ext = ".jpg"

path += "\\**\\"

for p in [i for i in glob(path)]:
    search_path = p + "*" + ext
    folder_name = os.path.basename(p.rstrip(os.sep))
    print(folder_name)
    if len([i for i in glob(search_path)]) == 0:
        continue
    else:
        with open(folder_name + ".pdf", "wb") as files:
            files.write(img2pdf.convert([i for i in glob(search_path)]))
