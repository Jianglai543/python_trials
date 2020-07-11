class SimpleGradeBook(object):
    def __init__(self):
        self.grade = {}

    def add_student(self, name):
        self.grade[name] = []

    def report_grade(self, name, score):
        self.grade[name].append(score)
        print(self.grade)

    def calculate_average(self, name):
        total = 0
        for i in self.grade[name]:
            total += i
        return total/len(self.grade[name])

class BySubjectGradeBook(object):
    def __init__(self):
        self.grade = {}

    def add_student(self, name):
        self.grade[name] = {}  # 名字的键作为存科目，成绩字典

    def report_grade(self, name, subject, score):
        by_subject = self.grade[name]  # 获取字典
        grades_value = by_subject.setdefault(subject, [])  # 创建多值字典
        grades_value.append(score)

    def calculate_average(self, name):
        by_subject2 = self.grade[name]
        total = 0
        len_subjects = 0
        for i in by_subject2.values():
            total += sum(i)
            len_subjects += len(i)
            # len_subjects += len(by_subject2)  错误写法！！字典长度不等于科目长度
        print(len_subjects)
        print(by_subject2)
        return total/len_subjects


if __name__ == '__main__':
    # a = SimpleGradeBook()
    a = BySubjectGradeBook()
    a.add_student('aaa')
    a.report_grade('aaa', 'maths', 90)
    a.report_grade('aaa', 'maths', 70)
    a.report_grade('aaa', 'Eng', 90)
    a.report_grade('aaa', 'Eng', 90)
    print(a.calculate_average('aaa'))

    grades_tuple = []
    grades_tuple.append((30,5))
    grades_tuple.append((40,5))
    total_grade = sum(grades * value for grades, value in grades_tuple)
    total_value = sum(values for _, values in grades_tuple)
    print(total_value, total_grade)