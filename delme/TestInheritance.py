class BaseRlsRecord:
    def typename(self,x):
        return type(x).__name__
    def get_type_name_of_subclass(self):
        return self.typename(self)

class Person(BaseRlsRecord):
    pass

print(Person().get_type_name_of_subclass())
