class Book:
    def __init__(self, bookId, bookName, pubId, price):
        self.bookId = bookId
        self.bookName = bookName
        self.pubId = pubId
        self.price = price

    def display(self):
        print(f"《{self.bookName}》书编号为{self.bookId}，出版社编号{self.pubId}，价格{self.price}")


b1 = Book(1, "高等数学", 3, 39.6)
b2 = Book(2, "民间艺术", 8, 27.9)

b1.display()
b2.display()
