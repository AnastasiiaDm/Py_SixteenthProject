'''2. Создать класс, описывающий группу студентов - `Group`. Данный класс хранит студентов в виде списка объектов `Student`
 также реализованного в виде соответствующего класса.
В классах реализовать необходимай набор атрибутов (Например класс `Student` должен иметь атрибуты `name`, `age`, `grades`),
 а так же необходимый набор методов экземпляра для работы с этими экземплярами.
'''

class Group:
    name = "Group #1"
    class Student:
            name = "Greg"
            age = "18"
            grades = str([6, 6, 1, 4, 9, 9, 10, 4])

            def characteristics(self):
                print(Group.name + '\n' + self.name + '\nage: ' + self.age + '\ngrads: ' + self.grades)

student = Group.Student()
student.characteristics()




