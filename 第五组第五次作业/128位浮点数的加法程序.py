from decimal import Decimal, getcontext

def validate_float(input_str):
    try:
        num = Decimal(input_str)
        return True
    except:
        return False

def add_floats(str1, str2):
    if not (validate_float(str1) and validate_float(str2)):
        return "Invalid input"

    getcontext().prec = 34  # 设置精度为128位（34位有效数字）
    num1 = Decimal(str1)
    num2 = Decimal(str2)
    result = num1 + num2
    return result

input1 = input("请输入第一个128位浮点数：")
input2 = input("请输入第二个128位浮点数：")

print("输入的两个浮点数相加的结果为：", add_floats(input1, input2))
