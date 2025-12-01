class MyList:
    def __init__(self, obj):
        self.data = obj[:]

    def __add__(self, other):
        l1 = len(self.data)
        l2 = len(other.data)
        data = []
        if l1 > l2:
            for i in range(l2):
                data.append(self.data[i] + other.data[i])
            for i in range(l2, l1):
                data.append(self.data[i])
        else:
            for i in range(l1):
                data.append(self.data[i] + other.data[i])
            for i in range(l1, l2):
                data.append(other.data[i])
        return MyList(data[:])


list1 = MyList([1, 2, 3, 4, 5])
list2 = MyList([3, 2, 1])
list3 = list1 + list2
print(list3.data)
