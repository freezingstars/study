class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance  # 私有属性

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"成功存入：{amount} 元")
        else:
            print("存入金额必须大于0！")

    def withdraw(self, amount):
        if amount <= 0:
            print("取款金额必须大于0！")
        elif amount > self.__balance:
            print("余额不足，取款失败！")
        else:
            self.__balance -= amount
            print(f"成功取出：{amount} 元")

    def get_balance(self):
        print(f"当前余额：{self.__balance} 元")


# ATM 菜单循环
def atm_system():
    account = BankAccount(1000)  # 初始余额，可自定义

    while True:
        print("\n======= ATM 系统 =======")
        print("1. 查询余额")
        print("2. 存款")
        print("3. 取款")
        print("4. 退出系统")
        print("========================")

        choice = input("请输入选项：")

        if choice == "1":
            account.get_balance()

        elif choice == "2":
            amount = float(input("请输入存款金额："))
            account.deposit(amount)

        elif choice == "3":
            amount = float(input("请输入取款金额："))
            account.withdraw(amount)

        elif choice == "4":
            print("感谢使用 ATM 系统，再见！")
            break

        else:
            print("无效选项，请重新选择！")

atm_system()

peach = 1
for i in range(9):
    peach = 2 * (peach + 1)
print(peach)
