class goa:
    name=""
    drink=""
    def party(self):
        print("Let's party...")
    def beach(self):
        print("Enjoy the beach...")

Ramesh=goa()
Suresh=goa()
Ramesh.party()
Suresh.beach()
Ramesh.name="Ramesh"
Suresh.name="Suresh"


Ramesh.drink="Yes"
Suresh.drink="No"
print(Ramesh.name)
print("drink:",Ramesh.drink)
print(Suresh.name)
print("drink:",Suresh.drink)
