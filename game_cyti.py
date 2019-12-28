import random
already_been = []


def read():
    my_file = open('city.txt', 'r', encoding='cp1251')
    cities = []
    for i in my_file.readlines():
        cities.append(i.upper()[0:-1])
    return cities


def computer_response(letter, city_list):
    res = [comp_city for comp_city in city_list if comp_city[0].upper() == letter]
    if res:
        answer = random.choice(res)
        computer_answer = 'Ответ компьютера {}\nПоследняя буква: {}'.format(answer, answer[-1])
        print(computer_answer)
        comp_res = [comp_city for comp_city in city_list if comp_city[0].upper() == answer[-1]]
        city_list.remove(answer)
        if comp_res:
            kwarg = {'string': computer_answer, 'comp_city': answer, 'last_letter': answer[-1]}
            return kwarg
        else:
            computer_answer = 'Вы проиграли!(\nГородов на букву {} больше нет'.format(letter)
    else:
        computer_answer = 'Городов на букву {} больше нет.\nВы выиграли!))'.format(letter)
    print(computer_answer)
    kwarg = {'string': computer_answer, 'comp_city': False, 'last_letter': letter}
    return kwarg


def check(city_list, city, letter):
    if letter == city[0] or letter == '':
        if city in city_list:
            letter = city[-1]
            print('Такой город есть.\nПоследняя буква:', letter)
            city_list.remove(city)
            already_been.append(city)
            dict_computer = computer_response(letter, city_list)
            letter = dict_computer['last_letter']
            return dict_computer
        else:
            if city in already_been:
                hint = 'Такой город был!\nПопробуйте еще раз.'
            else:
                hint = 'Такого города нет.'
    else:
        hint = 'Нужно ввести город на букву {}'.format(letter)
    print(hint)
    return {'string': hint, 'comp_city': False}


if __name__ == "__main__":
    already_been = []
    last_letter = ''
    city_list = read()
    while True:
        my_city = input("Введите название города: ").upper()
        response = check(city_list, my_city, last_letter)
        if not response['comp_city']:
            exit()

