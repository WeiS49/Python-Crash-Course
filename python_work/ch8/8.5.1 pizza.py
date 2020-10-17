
def make_pizza(*toppings, size = '7'):
    print(toppings, size)

make_pizza('junk', 'mushroom', 'pepper')    # 不指定参数名情况下, 所有传入参数均被元组封装

def make_pizza(size = '7', *toppings):
    print(toppings, size)

make_pizza('junk', 'mushroom', 'pepper')    # 第一个传入值作为size值, 其他值被元组封装

