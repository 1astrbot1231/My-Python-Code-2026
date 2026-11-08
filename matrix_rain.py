import random
import time
import os
import sys

# Windows清屏命令
os.system('cls')

# 包含数字、字母和一些符号的字符集
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+{}|:<>?~"
columns = 100 # 模拟的宽度

try:
    while True:
        # 随机生成一行字符
        line = ""
        for _ in range(columns):
            line += random.choice(chars)
            # 随机加点空格让看起来更错落有致
            if random.random() > 0.7:
                line += " "
            else:
                line += random.choice(chars)
        
        # \033[92m 是绿色，\033[0m 是恢复
        print("\033[92m" + line[:100] + "\033[0m")
        
        # 控制下落速度，越小越快
        time.sleep(0.05)
except KeyboardInterrupt:
    # 按 Ctrl+C 停止
    print("\033[0m\n[系统已切断连接]")