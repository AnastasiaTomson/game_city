import random
my_file = open('city.txt', 'r', encoding='cp1251')

city_list = []
already_been = []
last_letter = ''
for i in my_file.readlines():
    city_list.append(i.upper()[0:-1])


def computer_response(letter):
    res = [comp_city for comp_city in city_list if comp_city[0].upper() == letter]
    if res:
        answer = random.choice(res)
        computer_answer = 'Ответ компьютера {} \n Последняя буква: {}'.format(answer, answer[-1])
        kwarg = {'string': computer_answer, 'last_letter': answer[-1]}
        return kwarg
    else:
        print('Городов на букву {} больше нет. Вы выиграли!'.format(letter))
        exit()


while True:
    my_city = input("Введите название города _____ ").upper()
    if last_letter == my_city[0] or last_letter == '':
        if my_city in city_list:
            last_letter = my_city[-1]
            print('Такой город есть. Последняя буква:', last_letter)
            city_list.remove(my_city)
            already_been.append(my_city)
            dict_computer = computer_response(last_letter)
            print(dict_computer['string'])
            if len(dict_computer) == 2:
                last_letter = dict_computer['last_letter']
        else:
            if my_city in already_been:
                print('Такой город был! Попробуйте еще раз.')
            else:
                print('Такого города нет.')
    else:
        print('Нужно ввести город на букву {}'.format(last_letter))
