#private variable and accessing
#private variable outside of the class

class Priv_Im:
    def __init__(self,abc):
        self.__abc=abc
    def get_abc(self):
        return self.__abc
    def set_abc(self,abc):
        return self.__abc
obj=Priv_Im(23)
print(obj._Priv_Im__abc)
print(obj.get_abc())
