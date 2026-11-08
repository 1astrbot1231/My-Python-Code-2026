def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # 处理字母（大小写）
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

print("=== 赛博特工加密系统 ===")
choice = input("输入 1 加密，输入 2 解密: ")

if choice == '1':
    msg = input("输入你要加密的机密: ")
    # 位移 3 位
    encrypted = caesar_cipher(msg, 3) 
    print(f"\n\033[92m密文: {encrypted}\033[0m")
    
elif choice == '2':
    msg = input("输入你要解密的乱码: ")
    decrypted = caesar_cipher(msg, -3)
    print(f"\n\033[93m明文: {decrypted}\033[0m")
else:
    print("输入错误，特工系统已自毁！")
