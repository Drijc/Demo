# from unicodedata import name


class garage:
    # dunder methods in python 
    def __init__(self,name) -> None:
        self.name=name

# this is also example of dunder methods in python 
    def __len__(self):
        return len(self.name)


# This is the following __len__ dunder method and is called as an built in function for exmaple len()
# And it is not called as my_object.__len__   

G=garage("drij")
print(len(G))


# inheritance exmaple

class Emp():
    def __init__(self, id, name, Add):
        self.id = id
        self.name = name
        self.Add = Add
 
# Class freelancer inherits EMP
class Freelance(Emp):

    def __init__(self, id, name, Add, Emails):
    

        # to inherit the followinf attribute from the parent class we make use of the super keyword
        # Also we make use of the following inheritance to reduce of the repetetion of the following declaration of the attribute
    
        super().__init__(id,name,Add)
        self.Emails = Emails

    @property
    def prnt(self):
        print(f"The following atribute are as follow {self.name} , {self.id}, {self.Add}, {self.Emails}")
 
Emp_1 = Freelance(103, "Suraj kr gupta", "Noida" , "KKK@gmails")

#if want to access the value without using () than we have to define the @property decorator. 

Emp_1.prnt


print('The ID is:', Emp_1.id)
print('The Name is:', Emp_1.name)
print('The Address is:', Emp_1.Add)
print('The Emails is:', Emp_1.Emails)