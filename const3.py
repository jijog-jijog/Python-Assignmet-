class teacher:
    def __init__(self,name,reno) -> None:
        self.name=name
        self.reno=reno
    def display(self):
        print("name=",self.name)
        print("reno=",self.reno)
t1=teacher(name="Ajish",reno="4567")
t2=teacher(name="Anish",reno="7654")
print(t1.name)
print(t2.reno)
t2.display()