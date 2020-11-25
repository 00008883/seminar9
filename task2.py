class Student:
    def __init__(self, id, marks):
        self.id = id
        self.marks = marks

    def calculate_average(self):
        total = 0
        for key in self.marks:
            total = total + self.marks[key]
        average = total / len(self.marks)
        return average

    def display_average(self):
        print(self.calculate_average())

if __name__ == '__main__':
    student1 = Student(1234, {'CSF': 75, 'FunPro': 80, 'WT': 85})
    student1.display_average()