tasklist = {}

# Ввод 1 элемента
taskdate = input("Введите дату: ")
taskvalue = input("Введите задачу: ")
tasklist[taskdate] = taskvalue

# Ввод 2 элемента
taskdate = input("Введите дату: ")
taskvalue = input("Введите задачу: ")
tasklist[taskdate] = taskvalue

# Ввод 3 элемента
taskdate = input("Введите дату: ")
taskvalue = input("Введите задачу: ")
tasklist[taskdate] = taskvalue

# print(tasklist)
# print(type(tasklist))
# print(len(tasklist))


''''# from collections import defaultdict

print("Please input three dates with tasks respectively")
# task_list = defaultdict(list)
task_list = {}
tasks = []

# date = input("Введите дату:")
# taskinput = input("Введите задачу:")
# task_list[date].append(taskinput)
#
# date = input("Введите дату:")
# taskinput = input("Введите задачу:")
# task_list[date].append(taskinput)
#
# date = input("Введите дату:")
# taskinput = input("Введите задачу:")
# task_list[date].append(taskinput)

# Начинаем блок сбора данных и сохранения их в словаре со списком значений
date = input("Введите дату:")
taskinput = input("Введите задачу:")

if date in task_list:
    task_list[date].append(taskinput)
else:
    task_list[date] = [taskinput]

# Начинаем блок сбора данных и сохранения их в словаре со списком значений
date = input("Введите дату:")
taskinput = input("Введите задачу:")

if date in task_list:
    task_list[date].append(taskinput)
else:
    task_list[date] = [taskinput]

# Начинаем блок сбора данных и сохранения их в словаре со списком значений
date = input("Введите дату:")
taskinput = input("Введите задачу:")

if date in task_list:
    task_list[date].append(taskinput)
else:
    task_list[date] = [taskinput]

print("Ключи: ", task_list.keys())
print("Значения: ", task_list.values())

print(task_list)
'''

