class calculator:
    def __init__(self,num1,num2) -> None:
        self.a=num1
        self.b=num2
    def add(self):
        print(self.a+self.b)
    def sub(self):
        print(a-b)
    def mul(self):
        print(a*b)
a=calculator(num1=int(input("Enter a num1:")),
             num2=int(input("Enter the num2:")))
b=calculator(input("Enter the option :"))
if(b=="a.add()"):
    a.add()
   