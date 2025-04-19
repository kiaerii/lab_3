#5
class Student:
    def __init__(self, name, surname, student_id):
        self.name=name
        self.surname=surname
        self.student_id=student_id
        self.grades=[]

    def __str__(self):
        return f"Student(name='{self.name}', surname='{self.surname}', student_id={self.student_id}, grades={self.grades})"

    def __eq__(self, other): #проверка на равенство айди
        if isinstance(other, Student): #является ли other объектом класса Student
            return self.student_id==other.student_id
        return False

    def __len__(self):
        return len(self.grades)

student1 = Student('Екатерина', 'Безбородова', 8)
student1.grades = [5, 4, 5]

student2 = Student('Ольга', 'Калашникова', 8)
student2.grades = [4, 5, 5]

print(student1)  #Вызов __str__ 
print(student1 == student2)  #Вызов __eq__ #true - id совпадает
print(len(student1))  #Вызов __len__ (кол-во оценок)
