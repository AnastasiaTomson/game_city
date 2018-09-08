import random
my_file = open('cyti3.txt', 'r')
cyti_list_row = my_file.readlines()

cyti_list = []
for i in cyti_list_row:
    cyti_list.append(i.upper()[0:-1])

my_cyti = input("Введите первое название города _____ ")
my_cyti = my_cyti.upper()

while True:


        if my_cyti in cyti_list:

            print('Такой город есть. Последняя буква:', my_cyti[-1])
            my_cyti_index = cyti_list.index(my_cyti)
            cyti_list.remove(my_cyti)
            cyti_list.insert(my_cyti_index, my_cyti + '1')


        else:
            print('Такого города нет.')
            my_cyti = input('Введите название города _____')
            my_cyti = my_cyti.upper()
            continue


        comp_cyti_list = []
        for i in cyti_list:
            if i[0] == my_cyti[-1] and i[-1] != '1':
                comp_cyti_list.append(i)
            elif i[0] != my_cyti[-1]:
                continue
            elif i[0] == my_cyti[-1] and i[-1] == '1':
                continue
        try:
            comp_answer = random.choice(comp_cyti_list)
        except IndexError:
            print('Городов на букву', my_cyti[-1], 'больше нет. Вы выиграли!')
            break
        print('Ответ компьютера', comp_answer, '\n', 'Последняя буква:', comp_answer[-1])
        comp_answer_index = cyti_list.index(comp_answer)
        cyti_list.remove(comp_answer)
        cyti_list.insert(comp_answer_index, comp_answer + '1')




        x = 0
        while x < 1:
            my_cyti = input('Введите город_____')
            my_cyti = my_cyti.upper()
            if my_cyti[0] == comp_answer[-1]:

                if my_cyti + '1' in cyti_list:
                    print('Такой город был')

                else:
                    x += 2
            else:
                print('Введите город на букву:', comp_answer[-1])














