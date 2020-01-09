# 阶乘实例

# 通过用户输入的数字计算阶乘

# 获取用户输入的数字
num = int(input("请输入数字:"))
factorial = 1

# 查看数字是负数,0 或正数
if num < 1:
    print("负数没有阶乘")
elif num == 0:
    print("0 的阶乘为1")
else:
    for i in range(1,num+1):
        factorial = factorial * i
    print("{}的阶乘为{}".format(num,factorial))
