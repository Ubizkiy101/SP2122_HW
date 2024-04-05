from teacher import Teacher
from student import Student
yaroslav = Teacher("Yaroslav", 45, 'Math', "Teacher")
oleksandr = Student("Oleksandr", 12,"SP2122", 15000)
denys = Student("Denys", 11,"SP2122", 16000)
dmytro = Student("Dmytro", 13,"SP2122", 5000)
kyrylo = Student("Kyrylo", 14,"SP2122", 4000)
humans = list()
for human in kyrylo, dmytro, denys, oleksandr, yaroslav:
    humans.append(human)
for human in humans:
    print(human)