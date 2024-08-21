my_dict = {"Den":1998,"Oleg":1997}
print(my_dict)
print(my_dict.get("Den"))
print(my_dict.get("Anton"))
my_dict.update({"Anton":1995,"Dima":1987})
F= my_dict.pop("Oleg")
print(F)
print(my_dict)

my_set = {1,2,1.5,2,'a',1.5,1,1,'a','b'}
print(my_set)
my_set.update({0,"C"})
my_set.discard(1)
print(my_set)