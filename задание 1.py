#1
class Student:
    def __init__(self, name,student_id):
        self.name=name
        self.student_id=student_id
        self.grades=[]

    def add_grade(self, grade): #оценка 0-10
        if 0<=grade<=10:
            self.grades.append(grade)
        else:
            print('Ошибка. Оценка не в диапазоне 0-10')
    def get_average(self): #средний балл
        if not self.grades:
            return 0.0
        return sum(self.grades)/len(self.grades)
    def display_info(self):
        print(f'Студент: {self.name}')
        print(f'ID: {self.student_id}')
        print(f"Оценки: {', '.join(map(str,self.grades))}")
        print(f'Средний балл: {self.get_average():.2f}\n') #.2f-округлить 2 знака после запятой
if __name__=="__main__":
    student1 = Student("Екатерина Безбородова", "888")
    student1.add_grade(5)
    student1.add_grade(6)
    student1.display_info()
