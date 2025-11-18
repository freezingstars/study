book_ls = []


def print_sysinfo():
    print('*' * 30)
    print('图书信息系统')
    print('1.显示图书信息')
    print('2.增加图书信息')
    print('3.修改图书信息')
    print('4.删除图书信息')
    print('5.退出系统')
    print('*' * 30)


def have_book(bid):
    for line in book_ls:
        if line[0] == bid:
            print('图书编号已存在！')
            return True
    return False


def show_book():
    print(f"{'id':<10}\t{'book':<25}")
    for bid, name in book_ls:
        print(f"{bid:<10}\t{name:<25}")


def delete_book(bid):
    for i, line in enumerate(book_ls):
        if line[0] == bid:
            del book_ls[i]
            print(f'编号{bid}的图书已成功删除！')
            return
    print('图书编号不存在！')


def insert_book():
    bid = input('请输入图书编号：')
    name = input('请输入图书名称：')
    if not have_book(bid):
        book_ls.append([bid, name])
        print(f'图书《{name}》已成功添加！')


def update_book(bid):
    for line in book_ls:
        if line[0] == bid:
            new_name = input('请输入更新后的图书名称：')
            line[1] = new_name
            print(f'编号{bid}的图书名称已更新为《{new_name}》！')
            return
    print('图书编号不存在！')


def main():
    while True:
        print_sysinfo()
        num = input('请选择功能（1-5）：')

        if num == '1':
            show_book()
        elif num == '2':
            insert_book()
        elif num == '3':
            bid = input('请输入要修改的图书编号：')
            update_book(bid)
        elif num == '4':
            bid = input('请输入要删除的图书编号：')
            delete_book(bid)
        elif num == '5':
            if input('确认退出(Yes or No):') == 'Yes':
                break
        else:
            print('输入有误，请重新输入！')


if __name__ == '__main__':
    main()
