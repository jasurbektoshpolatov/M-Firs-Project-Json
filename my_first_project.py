import json

with open('questions.json') as file:
    questions_load = json.load(file)
ranks = []
names = []

while True:

    questions = input("Do you want to play? yes or no?: ")
    if questions == 'yes':
        name = input('Write your name here: ')
        print(f"Hello {name}, Welcome to my game who wants to Billionare! ")
        names.append(name)
        back = []

        while True:

            n = 0
            options = int(input("To pass the test put 1: \n\nTo see the ranks of the game put 2: \n\nTo leave game put 3: \n\nPut here: "))
            if options == 1:
                exp = [True]
                abcd = 'abcd'

                for n in range(len(questions_load)):
                    if exp[n] == True:
                        get_questions = questions_load[n].get('question')

                        print(get_questions)
                        get_answers = questions_load[n].get('answers')
                        get_options = [v for v in abcd]
                        get_options_answer = [j['key'] for j in get_answers]
                        get_Trues = [b.get("isTrue") for b in get_answers]
                        for i in range(len(get_options_answer)):
                            print(f'{abcd[i]}. {get_options_answer[i]}')
                        users_answer = str(input("Put your answer here: "))
                        for f in range(len(get_options_answer)):
                            if users_answer == get_options[f]:
                                get_Trues1 = get_Trues[f]
                                exp.append(get_Trues[f])

                    else:
                        print("You choose wrong answer! ")
                        break
                back.append(exp)

            elif options == 2:

                for x in back:
                    ranks.append(x[1:].count(True))
                    zips = zip(names, ranks)
                    dicts = dict(zips)
                    for d, y in dicts.items():
                        print(f"{d} - {y}")

                    # lists = []
                    my_dict = dict(zip(names, ranks))
                    # lists.append(my_dict) # You can also appen to list and dump to Json in Array type
                    with open('users.json', 'a', encoding='utf-8') as row:
                        json.dump(my_dict, row)

            elif options == 3:
                break

    else:
        print('You succesfully left from the game!')
        break