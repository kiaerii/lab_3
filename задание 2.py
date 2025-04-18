class Person:
    def __init__(self, name,age):
        self.name=name
        self.age=age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def __str__(self):
        return f"Student(name={self.name}, age={self.age}, id={self.student_id})"

class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age) #super-вызывает объект родительского класса, избегая дублирования и ошибок
        self.subject=subject 
        self.students=[]

    def add_student(self, student): #добавляет студента в список
        if student not in self.students:
            self.students.append(student)
            print(f'Студент {student.name} добавлен к преподавателю {self.name}')
        else:
            print(f'Студент {student.name} уже есть у преподавателя {self.name}')
    
    def remove_student(self, student): #удаляет студента из списка
        if student in self.students:
            self.students.remove(student)
            print(f'Студент {student.name} удален у преподавателя {self.name}')
        else:
            print(f'Студента {student.name} нет у преподавателя {self.name}')
    
    def list_students(self): #удаляет студента из списка
        print(f'\nСписок студентов преподавателя {self.name} ({self.subject}):')
        if not self.students:
            print('нет студентов')
        else:
            for student in self.students:
                print(f'{student.name}')

if __name__ == "__main__": #создаем студентов
    student1 = Student('Безбородова Екатерина',18, '888')
    student2 = Student('Калашникова Ольга',19, '999')

    #создаем преподавателя
    teacher = Teacher('Светлана Ивановна', 45, 'Математика')

    #добавляем студентов
    teacher.add_student(student1)
    teacher.add_student(student2)
    teacher.add_student(student2) #попытка добавить повторно

    #выводим список
    teacher.list_students()

    #удаляем студента
    teacher.remove_student(student1)
    teacher.remove_student(student1)  #попытка удалить повторно

    #выводим обновленный список
    teacher.list_students()
        
        
