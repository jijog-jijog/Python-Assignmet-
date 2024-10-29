class student:
    def __int__(self):

      self.name="Anish"
      self.register="98567"
    def display(self):
        print("Name=",self.name)
        print("register=",self.register)
s1=student()
s2=student()
s1.name="Jijo"
s1.register="2456"
s2.name="Gino"
s2.register="9876"
print(s2.name)
s1.display()
s2.display()
