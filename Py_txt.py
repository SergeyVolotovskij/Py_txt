from datetime import *
from colorama import init #для стиля ветового
from colorama import Fore, Back, Style #для стиля ветового
init()#для стиля цветового

""" Cоздает новый файл именуя его как "task" + _тек.дата.txt """
datenow = datetime.today().strftime(" %d.%m.%Y") #дата-месяц-год
filename = "Task" + "_" + str(datenow) + ".txt"

#ДОБАВЛЯЕМ ПРОВЕРКУ - СУЩЕСТВУЕТ УЖЕ ТАКОЙ ФАЙЛ ИЛИ НЕТ?
try:
    file = open(filename, "r")
except FileNotFoundError: #ЕСЛИ ФАЙЛА НЕТУ - ТОГДА...
    print("Файл отсутствует - формирую новый!")
    file = open(filename, "w") #СОЗДАЕМ ФАЙЛ

    #ОТКРЫВАЕМ ФАЙЛ ДЛЯ ЗАПОЛНЕНИЯ ШАПКИ
    file = open(filename,"a")
    file.write(('{0:*^20}').format(datenow + "г. "))
    file.write("\n" + "========================================" + "\n")
    file.close()

def write_file():
    """ Функция производит запись информации, введенную пользователем в файл методом
    добавления """
    print(Fore.YELLOW)
    info = input("КАКУЮ ИНФОРМАЦИЮ ВВЕСТИ? ")
    info1 = input("ВАЖНО? ")
    file = open(filename, "a")

    if info1 == "да":
        file.write("!" + "*" + ". " + info + ".\n")

    elif info1 == "да1":
        file.write("!" + "*" + ". " + info + ".\n")
        file = open(filename, "r")

        print(Fore.BLUE)
        print(file.read()) #Выводим инфо с файла в консоль!!!

    else:
        file.write("*" + ". " + info + ".\n")

    print(Fore.GREEN)
    print("ИНФОРМАЦИЯ ВНЕСЕНА!")
    file.close()

while 1 == 1:
	write_file()

