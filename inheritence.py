class A:
    def __init__(self):
        print("in init A")
    def feature1(self):
        print("in feature1")
    def feature2(self):
        print("in feature2")

class B:

    def __init__(self):
        print("in init B")
        super().__init__()
    def feature3(self):
        print("in feature3")
    def feature4(self):
        print("in feature4")

class C(A,B):
    def __init__(self):
        print("in init C")
        super().__init__()                                #method resolution order(MRO)
    def feature5(self):
        print("in feature5")
    def feature6(self):
        print("in feature6")


a1=C()
a1.feature1()





