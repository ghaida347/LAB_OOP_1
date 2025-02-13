class Panda:
    
    def __init__(self, Oper:str, number1:int, number2:int, user_name:str):
        self.Oper=Oper
        self.number1=number1
        self.number2=number2
        self.user_name=user_name
        
    
    def operation(self):
        if self.Oper=="summation":
            result= self.number1+self.number2
        elif self.Oper=="subtract":
            result=self.number1-self.number2
        elif self.Oper=="multiply":
            result=self.number1*self.number2 
        elif self.Oper=="divide":
            result=self.number1/self.number2
        else:
            print("The no operation by this name , please enter the correct operation name")
        Operatons=f"The operation is {self.Oper} , the result is {result} ,the first number is {self.number1} , the second number is {self.number2} , the user name is {self.user_name} "
        return Operatons
    
    
    def even_number(self):
        if self.number1 %2==0:
            print(f"{self.number1} is even")
        else:
            print(f"{self.number1} is not even")
        if self.number2 %2==0:
            print(f"{self.number2} is even")
        else:
            print(f"{self.number2} is not even")
            
            
            
Panda1= Panda("summation",10, 20, "ghaida")
Panda2= Panda("subtract",70 , 50, "nawal")
Panda3 =Panda("multiply", 5, 6, "ghada")
Panda4 = Panda("divide", 100, 5, "lwlw")
print(Panda1.operation())
print(Panda2.operation())
print(Panda3.operation())
print(Panda4.operation())


print(Panda1.even_number())
print(Panda2.even_number())
print(Panda3.even_number())
print(Panda4.even_number())
