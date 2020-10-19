
# from .. import pizza as p
# p.make_pizza(12, 'cheese')

# from .. import pizza

# import os
# import sys
# xs = sys.path
# sys.path.append(os.getcwd())
# sys.path.append("...")

# for x in xs:
#     print(x)

# from python_work.ch8 import pizza
# from .. import pizza

# from pizza import make_pizza

# import pizza as p

# p.make_pizza(12, 'test')

# from ch8.pizza import make_pizza

# make_pizza(12, 'test')

# from python_work.ch8.pizza import make_pizza


# import sys

# sys.path.append('.')    # 添加工作区

# paths = sys.path
# for path in paths:
#     print(path)

# import site
# print(site.getsitepackages())

# from python_work.ch8 import pizza
# pizza.make_pizza(12, 'mushroom')


# from python_work.ch8.module.greeter import greet_user

from python_work.ch8.module import greeter  # 直接导入即可(因为已经将父目录添加进工作区)

greeter.greet_user()












