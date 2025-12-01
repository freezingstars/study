class Course:
    totalCredit = 0

    def __init__(self, course_id, course_name, credit, course_nature):
        self.courseId = course_id
        self.courseName = course_name
        self.credit = credit
        self.courseNature = course_nature
        Course.totalCredit += credit

    def display(self):
        print(f"《{self.courseName}》课程编号为{self.courseId}，{self.credit}学分，{self.courseNature}")

    @classmethod
    def display_credit(cls):
        print("总学分为：", cls.totalCredit)


c1 = Course(1, "Python程序开发", 4, "必修")
c2 = Course(2, "MySQL数据库技术", 2, "选修")

c1.display()
c2.display()

c1.display_credit()
Course.display_credit()

print("总学分为：", Course.totalCredit)
