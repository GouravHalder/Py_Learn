class Person:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def print_name(self):
        print (f'In Base class {self.first_name} {self.last_name}' )


class Person1:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def print_name(self):
        print (f'In Base1 class {self.first_name} {self.last_name}' )
    def print_lastname(self):
        print (f'In Base1 class last name {self.last_name}' )
class Programmer(Person,Person1):
    def __init__(self,first_name,last_name,fav_lang):
        #self.first_name=first_name
        #self.last_name=last_name
        super().__init__(first_name,last_name)
        self.fav_lang=fav_lang
    def print_name_lang(self):
        super().print_name()
        super().print_lastname()
        print(f'In Derived class {super().print_name()} loves {self.fav_lang}')


x=Programmer('Gourav','Halder','Python')
x.print_name_lang()
print (f'isinstance = {isinstance(x,Programmer)}')
print (f'issubclass = {issubclass(Programmer,Person)}')
print (f'issubclass = {issubclass(bool,float)}')
         