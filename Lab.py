from datetime import date
#naming conventions: PascalCase, always class is in indivisual, singular name
class Person:

    #initilizer/ constructor
    def __init__(self, name:str, gender:str, age:int) -> None:
        #addtributes/ properties
        self.name = name
        self.gender = gender
        self.age = age

    
    #methods
    def introduce(self):
        introduction = f"I am {self.name} , my gender is {self.gender} and I am {self.age} years old"
        return introduction


#creating instances/ objects

person1 = Person("Ahmed", "Male", 23)
person2 = Person("Nora", "Female", 25)

#calling a method
print(person1.introduce())
print(person2.introduce())

#accessing an attribute/peroperty
print(person1.gender)





#class for a task
class Task:

    def __init__(self, title:str, status:bool, due_date:date):
        self.title = title #public
        #self.__status = status #private
        self.set_status(status)
        self.due_date = due_date #public

    #setter
    def set_status(self, status):
        if not isinstance(status, bool):
            raise Exception("status can only be boolean")
        self.__status = status

    #getter
    def get_status(self):
        return self.__status


    def describe(self) -> str:
        return f"{self.title} - {self.get_status()} - {self.due_date}"
    


#instance
task1 = Task("do my homework", False, date(2024, 7, 1))
task2 = Task("Go to Liverpool match", False, date(2024, 8, 14))

task2.set_status(True)
print(task1.describe())
print(task2.describe())