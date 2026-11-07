print("=== 欢迎来到【不安全】的系统 ===")
# 我们设定正确的密码是 "123456"
correct_password = "123456"

# 接收你输入的密码
user_input = input("请输入密码: ")

# 模拟黑客网站的错误查询逻辑
# 如果用户输入的密码等于正确的，或者 1=1 成立，就通过
if user_input == correct_password or "OR 1=1" in user_input:
    print("【ACCESS GRANTED】恭喜，系统已被入侵，你进来了！")
else:
    print("【ACCESS DENIED】密码错误！")