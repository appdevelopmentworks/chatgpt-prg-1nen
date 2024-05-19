import PySimpleGUI as sg
import os
import google.generativeai as genai

GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

sg.theme("DarkBrown3")

selects1 = ["Python","Java","JavaSclipt","C++","Go","C#","pine","MQL4","Swift","Visual Basic",]

selects2 = ["言語の特徴","名前の起源","用途","便利な機能","隠れた機能","データ","バグ"]

layout = [[sg.T("言語の種類:"),sg.Combo(selects1, default_value=selects1[0], s=(15), k="cb1")],
          [sg.T("テーマ内容:"),sg.Combo(selects2, default_value=selects2[0], s=(15), k="cb2")],
          [sg.Im("futaba.png"),
           sg.T("これに関するトリビア書くよ。"),
           sg.B("実行", k="btn")],
          [sg.ML(k="txt", font=(None,14), s=(60,13))]]

win = sg.Window("プログラムのトリビア自動生成", layout, font=(None, 14), size=(550, 400))

def execute():
    role = "あなたは、優れた女子高生プログラマーです。親しい口調で話します。"
    prompt = f"プログラム言語が{v['cb1']}の{v['cb2']}に関するトリビアを1つ教えて。"
    prompt = role + prompt
    #
    win["txt"].update("")
    response = model.generate_content(prompt)
    win["txt"].update(response.text)
    win["txt"].update("\n【以上です】", append=True)

while True:
    e, v = win.read()
    if e == "btn":
        execute()
    if e == None:
        break
win.close()