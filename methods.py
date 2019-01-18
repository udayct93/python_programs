class student:
    school="jnv"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
         return  (self.m1+self.m2+self.m3)/3


   # def get_m1(self):                            #accessor
    #  return  self.m1

    #  def set_m1(self,value):                        #mutator
     #   slef.m1=value

    @classmethod                                      # we should use deecodators
    def getschool(cls):                                       # class method
        return cls.school

    @staticmethod                                      # static method
    def info():
        print("its a static method")


s1=student(75,74,84)
s2=student(45,63,55)

print(s1.avg())
print(s2.avg())

print(student.getschool())
print(student.info())