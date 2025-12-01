stu_info = []

def addStu(name: str, age: int, gender: str, show_all: bool = False):
    stu_info.append({
        "name": name,
        "age": age,
        "gender": gender
    })

    # 输出方式可控
    if show_all:
        print(stu_info)
    else:
        print(f"Added: {stu_info[-1]}")

# 调用
addStu("Chen", 4, "male")
addStu("Chen", 5, "male", show_all=True)
