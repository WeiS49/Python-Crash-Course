
from privileges import Admin # 导入模块会将其他代码一并导入(实例, 无关语句)
# from privileges import admin2 # 只会导入输出内容 单变量并没有直接导入


admin = Admin()
admin.privileges.show_privileges()

# admin2.privileges.show_privileges()







