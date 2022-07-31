class matriculation:
    students = []
    def __init__(self,number):
        self.number = number
        matriculation.students.append(self)

    @classmethod
    def show(cls):
        for student in matriculation.students:
            print(student.number, end= " ")
        print("\n")

    def mirror():
        pass

class course:
    def __init__(self,course):
        #super().__init__()
        self.course = course
        self.course_li.append(self)
    @classmethod
    def show(cls):
        for subject in course.course_li:
            print(subject.course, end= " ")
        print("\n")

def main():
    s1 = matriculation(1)
    s2 = matriculation(2)
    #print the list students
    """
    for student in matriculation.students:
        print(student.number, end= " ")
    """
    matriculation.show() #here I am calling the class method
    c1 = course("Math")
    c2 = course("History")
    #this is how you print the content: print(c2.course)
    course.show()

if __name__ == "__main__":
    main()

"""
a static method doesn’t know about the class itself. In a classmethod, the parameter is always the class itself.

a static method knows nothing about the class or instance. You can just as well use a function call.

a class method gets the class when the method is called. It knows abouts the classes attributes and methods.
calling a classmethod: classname.methodname()
calling a staticmethod:  classname.methodname()
# Calling static methods works on classes as well as instances of that class
Person.call_person()  # calling on class
p = Person()
p.call_person()       # calling on instance of class
"""
