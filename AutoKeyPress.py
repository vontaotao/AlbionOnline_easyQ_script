import pyautogui
import time
import keyboard
import threading
import tkinter as tk
from tkinter import messagebox, ttk

# 标记是否持续按键
pressing = False

# 持续按 Q 键的函数
def press_q_continuously(interval=1):
    global pressing
    while pressing:
        pyautogui.press('q')
        time.sleep(interval)

# 启动或停止持续按键的函数
def toggle_pressing():
    global pressing
    if not pressing:
        try:
            interval = float(interval_combo.get())
            pressing = True
            threading.Thread(target=press_q_continuously, args=(interval,), daemon=True).start()
        except ValueError:
            messagebox.showerror("输入错误", "请选择有效的间隔时间。")
    else:
        pressing = False

# 创建 GUI 界面
root = tk.Tk()
root.title("AlbionOnline Easy Q Script")

# 设置窗口图标
root.iconbitmap('custom_icon.ico')

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

# 自定义开始结束键标签和输入框
start_stop_label = tk.Label(frame, text="自定义开始结束键")
start_stop_label.grid(row=0, column=0, pady=5)
start_stop_entry = tk.Entry(frame)
start_stop_entry.insert(0, "s")
start_stop_entry.grid(row=0, column=1, pady=5)

# 间隔时间标签和下拉栏
interval_label = tk.Label(frame, text="间隔时间")
interval_label.grid(row=1, column=0, pady=5)
interval_combo = ttk.Combobox(frame, values=["1", "0.8", "0.6", "0.4", "0.2"])
interval_combo.set("1")
interval_combo.grid(row=1, column=1, pady=5)

# 开始按钮
start_button = tk.Button(frame, text="开始/停止", command=toggle_pressing)
start_button.grid(row=2, column=0, columnspan=2, pady=10)

# GitHub 链接
github_label = tk.Label(frame, text="开源地址: https://github.com/vontaotao/AlbionOnline_easyQ_script", fg="blue", cursor="hand2")
github_label.grid(row=3, column=0, columnspan=2, pady=5)
github_label.bind("<Button-1>", lambda e: root.clipboard_append("https://github.com/vontaotao/AlbionOnline_easyQ_script"))

# 绑定自定义按键来启动/停止持续按 Q 键
def on_key_event(e):
    if e.name == start_stop_entry.get():
        toggle_pressing()

keyboard.on_press(on_key_event)

root.mainloop()
