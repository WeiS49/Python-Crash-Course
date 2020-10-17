
def function1(parameter_0, parameter_1="hello"):    # 指定默认形参两边不要有空格
    print(parameter_1, parameter_0)

function1('value_0', parameter_1="value_1") # 同理, 关键字实参中也不能有空格                


def function2(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4, parameter_5,
        ):      # 参数太多装不下, 可以分行写

    print(parameter_0)
    print(parameter_1)
    print(parameter_2)
    print(parameter_3)
    print(parameter_4)
    print(parameter_5)


