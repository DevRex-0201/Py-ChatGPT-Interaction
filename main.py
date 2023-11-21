import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
import openai

# OpenAIの認証情報とモデルを設定します
openai.api_key = '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'  # あなた自身のAPIキーで置き換えてください
model_name = 'gpt-3.5-turbo'  # 使用するChatGPTモデルを指定します
responses = []

# Markdown入力を処理するための関数を定義します
def process_input():
    markdown_text = input_text.get("1.0", tk.END)
    prompt = markdown_text
    message = [{'role': 'user', 'content': f'{prompt}」\n このような結果を得るには、日本語でどのようなプロンプトを入力すればよいですか？ '}]
    # message = [{'role': 'user', 'content': f'{prompt}」\n このような結果を得るには、どのプロンプトを入力する必要がありますか？ 出力は日本語でお願いします。 質問に対応した基本的な答えだけを出力してください。私は日本人です。出力は必ず日本語にしてください。'}]
    response = openai.ChatCompletion.create(
    model="gpt-4",
    messages = message,
    temperature=0.2,
    max_tokens=800,
    frequency_penalty=0.0,
    timeout=1200
    )
    chatgpt_output = response.choices[0].message["content"].strip()

    # prompt_question=f'{prompt}"\n" 上記のテキストを入力したときに[{chatgpt_output}]の結果を出力するには、どのプロンプトを入力する必要がありますか？'
    # message2=[{"role": "user", "content": prompt_question}]
    # response2 = openai.ChatCompletion.create(
    # model="gpt-3.5-turbo",
    # messages = message2,
    # temperature=0.2,
    # max_tokens=700,
    # frequency_penalty=0.0,
    # timeout=1200
    # )
    # prompt_question_output=response2.choices[0].message["content"].strip()


    # prompt_question3=f'{prompt}\n 上記のマークダウンを同じテキストに変換してください。'  
    prompt_question3=f'{prompt}\n 上記のマークダウンをそのまま出力してください。' 
    message3=[{"role": "user", "content": prompt_question3}]
    response3 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages = message3
    )

    total_output=response3.choices[0].message["content"].strip()

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, total_output)
    
    prompt_text.delete("1.0", tk.END)
    prompt_text.insert(tk.END, chatgpt_output)

# Markdownをクリアするための関数を定義します
def clear_text(*text_widgets):
    for text_widget in text_widgets:
        text_widget.delete("1.0", tk.END)

# 会話をファイルに保存するための関数を定義します
def save_conversation():
    conversation = input_text.get("1.0", tk.END) + "\nChatGPT 出力:\n" + output_text.get("1.0", tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("テキストファイル", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(conversation)

# ファイルから会話を読み込むための関数を定義します
def load_conversation():
    file_path = filedialog.askopenfilename(filetypes=[("テキストファイル", "*.md")])
    if file_path:
        with open(file_path, "r") as file:
            conversation = file.read()
            clear_text(input_text, output_text)
            input_text.insert(tk.END, conversation)

# メインウィンドウを作成します
window = tk.Tk()
window.title("Markdown ChatGPT")

# Markdownオプションを備えた入力テキストエリアを作成します
input_text = ScrolledText(window, height=20, width=80, wrap=tk.WORD)
input_text.pack()

# 入力エリア用のラベルを作成します
input_label = tk.Label(window, text="Markdown入力（例: ## タイトル, **太字**, *斜体*)")
input_label.pack()

# Promptの表示用のTextウィジェットを作成します
prompt_text = ScrolledText(window, height=5, width=80, wrap=tk.WORD)
prompt_text.pack()
prompt_text.insert(tk.END, "ここにプロンプトが表示されます。")  # Initial prompt text

# 処理ボタンを作成します
process_button = tk.Button(window, text="処理", command=process_input)
process_button.pack()

# 出力エリア用のラベルを作成します
output_label = tk.Label(window, text="ChatGPT 出力:")
output_label.pack()

# 出力テキストエリアを作成します
output_text = ScrolledText(window, height=20, width=80, wrap=tk.WORD)
output_text.pack()

# ステータスバーを作成します
status_bar = tk.Label(window, text="準備完了", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# メニューバーを作成します
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# ファイルメニューを作成します
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="ファイル", menu=file_menu)
file_menu.add_command(label="新規", command=lambda: clear_text(input_text, output_text))
file_menu.add_command(label="開く", command=load_conversation)
file_menu.add_command(label="保存", command=save_conversation)
file_menu.add_separator()
file_menu.add_command(label="終了", command=window.quit)

# ヘルプメニューを作成します
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="ヘルプ", menu=help_menu)
help_menu.add_command(label="ヘルプ内容")

# メインのイベントループを開始します
window.mainloop()
