taskarray = []

# Ввод 1 элемента
taskdate = input("Введите дату: ")
taskvalue = input("Введите задачу: ")
taskarray.append([taskdate, taskvalue])

# Ввод 2 элемента
taskdate = input("Введите дату: ")
taskvalue = input("Введите задачу: ")
taskarray.append([taskdate, taskvalue])

# Ввод 3 элемента
taskdate = input("Введите дату: ")
taskvalue = input("Введите задачу: ")
taskarray.append([taskdate, taskvalue])

# Вывод всех 3 сохраненных ранее элементов
print(taskarray[0][0], taskarray[0][1])
print(taskarray[1][0], taskarray[1][1])
print(taskarray[2][0], taskarray[2][1])

