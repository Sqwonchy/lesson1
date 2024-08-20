immutable_var = (12, 1.5, '3й тип данных')
print(immutable_var)
# immutable_var[0]=15 объект tuple не поддерживает назначение элементов
print(immutable_var)


mutable_list = ["Яблоко","арбуз","картошка"]
mutable_list[2] = "дыня"
print(mutable_list)