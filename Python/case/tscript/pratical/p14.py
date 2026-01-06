def swipe(n):
    if n < 10:
        print(n)
    else:
        print(n % 10)      # ← 关键：先打印最低位
        swipe(n // 10)
        print(n % 10)


swipe(2837)