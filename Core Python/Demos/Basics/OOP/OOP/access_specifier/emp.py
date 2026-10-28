# class Emp:
#     def __init__(self,id,name,sal):
#         self.__id=id
#         self.__name=name
#         self.__sal=sal
#     def getId(self):
#         return self.__id
#     def setId(self,nid):
#         self.__id = nid
#     def __str__(self):
#         return f"Id = {self.__id} Name= {self.__name} Sal = {self.__sal}"

# class Hr(Emp):
#     def __str__(self):
#         print(self.__id)
#         return super().__str__()

# e1 = Emp(12,"Swaraj",1234)
# print(e1.getId())
# e1.setId(19)
# print(e1.getId())
# h1 = Hr(1,"Smriti",2345)



class Emp:
    def __init__(self,id,name,sal):
        self._id=id
        self._name=name
        self._sal=sal
    def getId(self):
        return self._id
    def setId(self,nid):
        self._id = nid
    def __str__(self):
        return f"Id = {self._id} Name= {self._name} Sal = {self._sal}"

class Hr(Emp):
    def __str__(self):
        print(self._id)
        return super()._str_()

e1 = Emp(12,"Swaraj",1234)
print(e1.getId())
e1.setId(19)
print(e1.getId())
h1 = Hr(1,"Smriti",2345)    