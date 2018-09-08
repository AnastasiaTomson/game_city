# ввод города
def a_function():
    my_city_index = city_list.index(my_city) #индекс города в списке
    last_letter = my_city[-1]
    if last_letter in ('Ь', 'Ы'):
        last_letter = my_city[-2]
    out_value = (my_city, last_letter, my_city_index)
    return out_value


# добавляем маркер
def b_function():
    city_list.remove(my_city)
    city_list.insert(my_city_cortege[2], my_city + '1')
    return city_list


# ответ компьютера
def c_function():
    for i in city_list:
        if i[0] == my_city_cortege[1] and i[-1] != '1':
            comp_list.append(i)
            random.shuffle(comp_list)
    return comp_list


# создаем рабочий список, без \n
def d_function():
    for i in initial_list:
        city_list.append(i.upper()[0:-1])
    return city_list

# добавляем к ответу компьютера +1 и перезаписываем лист city_list
def e_function():
    if my_city in city_list:
        my_city_index = city_list.index(my_city)
        city_list.remove(my_city)
        city_list.insert(my_city_index, my_city + '1')
    return city_list





import random
input_file = open('city.txt', 'r')
initial_list = input_file.readlines()
city_list = []
city_list = d_function()
while True:
    my_city = str(input().upper())
    for i in city_list:
        if i[0:-1] == my_city and i[-1] == '1':
            print('Данный город уже был. Введите другой город на букву: ', my_city_cortege[1])
            my_city = str(input().upper())

    if my_city in city_list:
        my_city_cortege = a_function()
        print('Введенный город: ', my_city_cortege[0] + '\n' + 'Последняя буква: ', my_city_cortege[1])
        city_list = b_function()
    else:
        print('Такого города нет.')
        my_city = str(input().upper())
        print(my_city[-1])
        continue
    comp_list = []
    comp_list = c_function()
    my_city = comp_list[0]
    my_city_cortege = a_function()
    city_list = e_function()
    print('Ответ компьютера', my_city_cortege[0] + '\n' + 'Последняя буква: ', my_city_cortege[1])







