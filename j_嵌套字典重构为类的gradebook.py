import collections


Grade = collections.namedtuple('Grade', ('score', 'weight'))

class Subject(object):

    def __init__(self):
        self.grade = []

    def report_grade(self, score, weight):
        self.grade.append(Grade(score, weight))

    def calculate_grade(self):
        total_grade = 0
        total_weight = 0

        for grade, weight in self.grade:
            total_grade += grade * weight
            total_weight += weight
        return total_grade / total_weight

class Student(object):

    def __init__(self):
        self.subs = {}

    def subject(self, name):
        if name not in self.subs:
            self.subs[name] = Subject()
        return self.subs[name]

    def calculate_grade(self):
        total = 0
        count = 0
        for grade in self.subs.values():
            total += grade.calculate_grade()
            count += 1
        return total / count

class GradeBook(object):

    def __init__(self):
        self._student = {}

    def student(self, name):
        if name not in self._student:
           self._student[name] = Student()
        return self._student[name]


if __name__ == '__main__':
    a = GradeBook()
    stu = a.student('aaaa')
    math = stu.subject('math')
    math.report_grade(100, 0.7)
    math.report_grade(90, 0.3)
    print(stu.calculate_grade())