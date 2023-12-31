from PIL import Image
import sys
import pyocr
import pyocr.builders

def scpy(screenshot): #画像から文字列に変換
    tools = pyocr.get_available_tools()
    tool = tools[0]

    langs = tool.get_available_languages()
    lang = langs[0]
    #txtに変換した文字列を代入する
    txt = tool.image_to_string(
        Image.open(screenshot),
        lang="eng",
        builder=pyocr.builders.TextBuilder(tesseract_layout=6)
    )
    Text = list(txt)   #文字列を配列に変換
    count = len(Text)
    i=0
    while True:   #寿司打の場合小文字アルファベットか'-'と'?'と','と'!'しか出てこないのでそれ以外の文字が出てきていたら削除する
        if i >= count:
            break
        if Text[i] < 'a' or Text[i] > 'z':
            if Text[i] !='-' and Text[i] !='?' and Text[i] !=',' and Text[i] !='!':
                del Text[i]
                count -= 1
            else:
                i += 1
        else:
            i += 1
    txt = str(''.join(Text))   #文字列に戻す
    print(f'{txt}を検出しました')
    return txt
