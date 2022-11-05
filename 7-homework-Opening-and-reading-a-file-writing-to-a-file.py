######################Задание №1######################################
def get_menu(recipe_file='recipes.txt'):
    cook_book = {}
    with open(recipe_file, encoding='utf8') as reps:
        for info in reps.read().split('\n\n'):
            dish, quantity_ingr, *ingr = info.split('\n')
            cook_book_list = []
            for ingridient in ingr:
                ingridient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x,
                                                         ingridient.split(' | '))
                cook_book_list.append({"ingridient_name": ingridient_name, "quantity": quantity, "measure": measure})
            cook_book[dish] = cook_book_list
        return cook_book


###########################Задание №2#####################################
def view_menu():
    for dish, ingridients in get_menu().items():
        print(f"\n{dish}:")
        for value in ingridients:
            print(f'      {value["ingridient_name"]} - {value["quantity"]} {value["measure"]}.')


def get_shoping_list_by_dishes(dishes, person_count):
    shoping_list = {}
    for dish in dishes:
        for ingridient in get_menu()[dish]:
            name_ingridient = ingridient.pop("ingridient_name")
            ingridient["quantity"] = (ingridient["quantity"]) * int(person_count)
            if name_ingridient in shoping_list:
                ingridient["quantity"] += shoping_list[name_ingridient]["quantity"]
            shoping_list.update({name_ingridient: ingridient})
    view_shoping_list_by_dishes(shoping_list)


def view_shoping_list_by_dishes(shoping_list):
    print("\nДля приготовления этих блюд на данное кол-во персон нам понадобиться:\n")
    index = 1
    for key, value in shoping_list.items():
        print(f'{index}. {key}: {value["quantity"]} {value["measure"]}.')
        index += 1
    print("\nЧто-то из ингридиентов можно найти на кухне, остальное придётся докупить.")


print("Добро пожаловать!!!\n")

command_help = ('Вам необходимо ввести команду, чтобы программа выполнила определённое действие:'
                '\nДоступyные команды: "1", "2", "9" "0"'
                '\n"1" - Показать меню'
                '\n"2" - Список ингридиентов для выбранного блюда на введённое кол-во персон'
                '\n"9" - Помощь по командам'
                '\n"0" - Закрыть программу')
print(command_help)
while True:
    print('\n=====================================================================================\n')
    commands = input('Введите команду: ')

    if commands == "1":
        view_menu()

    elif commands == "2":
        try:
            dish_request = input("Введите через запятую названия блюд с заглавной буквы: ").split(", ")
            persons = input("Введите на какое колличество персон нужно приготовить: ")
            get_shoping_list_by_dishes(dish_request, persons)
        except:
            print('Кажется Вы где-то ошиблись с вводом. Перепроверьте и введите заново, но без ошибок =)')

    elif commands == "9":
        print(command_help)

    elif commands == "0":
        print("Всего доброго, Запускайте ещё. Zzz")
        break
###########################Задание №3#####################################
import os

path = 'files/'


def files(path: str):
    files_list = os.listdir(path)
    files_dict = {}

    for file_name in files_list:
        fil_txt = file_name.rfind('.txt', -4)
        if fil_txt >= 0:
            with open(os.path.join(path, file_name), 'r', encoding='utf-8') as file:
                files_dict[file_name] = file.readlines()

    with open("combination.txt", 'w', encoding='utf-8') as file:
        for file_name, rows in sorted(files_dict.items(), key=lambda x: len(x[1])):
            file.write(f"Название файла: {str(file_name)} \n")
            file.write(f"Кол-во строк - {str(len(rows))} \n\n")
            if '\n' not in rows[-1]:
                rows[-1] += '\n\n'
            file.write(''.join(rows))


print('Файл "comnination.txt" успешно загружен')
files(path)