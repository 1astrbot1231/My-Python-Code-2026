import tkinter as tk
import time

def fake_bsod():
    # 创建全屏窗口
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg='#0078D7') # Windows经典蓝屏蓝

    # 蓝屏表情
    label_face = tk.Label(root, text=":(", font=("Segoe UI", 100), bg='#0078D7', fg='white')
    label_face.pack(pady=(100, 20))

    # 提示文字
    text = "你的电脑遇到问题，需要重新启动。\n我们只收集某些错误信息，然后为你重新启动。\n\n完成度: 99%"
    label_text = tk.Label(root, text=text, font=("Microsoft YaHei", 24), bg='#0078D7', fg='white', justify='left')
    label_text.pack(pady=20)

    # 假的错误代码
    err_text = "停止代码: CRITICAL_PROCESS_DIED\n失败的操作: Hacker_Invasion.sys"
    label_err = tk.Label(root, text=err_text, font=("Microsoft YaHei", 14), bg='#0078D7', fg='white', justify='left')
    label_err.pack(pady=50)

    # 按 Esc 退出
    root.bind("<Escape>", lambda e: root.destroy())
    root.mainloop()

fake_bsod()