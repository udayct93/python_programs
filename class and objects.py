class computer:
    def config(self):
        print("am in class nw")


com1=computer()
com2=computer()

com1.config()
com2.config()



class computer:
    def __init__(self):
        self.name="kudda"
        self.age=8

    # def update(self):
    #     self.age=30

    def compare(self,c2):
            if self.age==c2.age:
                return True
            else:
                return False



c1=computer()
c2=computer()

if c1.compare(c2):
    print("they r same")
else:
    print("diffirent")
print(c1.age)
print(c2.age)






