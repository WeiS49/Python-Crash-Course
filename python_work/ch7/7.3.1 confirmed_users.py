
# 7.3.1
# 在列表之间移动元素

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:    # 当该列表还有数据’‘
    current_user = unconfirmed_users.pop()

    print(f"Verifying user:{current_user.title()}")
    confirmed_users.append(current_user)

# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())   # 这里编辑器不知道添加进的数据类型, 所有没有语法高亮




