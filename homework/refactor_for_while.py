questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

counter = 0
counter_answer = 0
answer_try = 3

while True:
    welcome = input("Привет!\nПредлагаю проверить свои знания английского!\nНаберите 'ready', чтобы начать!\n")
    if welcome == "ready":
        break
    else:
        print("Кажется, вы не хотите играть. Очень жаль. Удачи")
        exit()

for i in range(len(questions)):
    print(questions[i])
    answer = input()
    if answer == answers[i]:
        print("Ответ верный!")
        counter += 1
    else:
        while answer != answers[i] and answer_try > 0:
            answer_try -= 1
            if answer_try == 0:
                print(f"Увы, но нет. Верный ответ: {answers[i]}")
                break
            print(f"Осталось попыток: {answer_try}, попробуйте еще раз!")
            answer = input()
        answer_try = 3



        # while answer != answers[i]:
        #     answer_try -= 1
        #     print(f"Осталось попыток: {answer_try}, попробуйте еще раз!")
        #     print(questions[i])
        #     answer = input()


    # while answer_try - 1:
    #     answer_try -= 1
    #     print(f"Осталось попыток: {answer_try} попробуйте еще раз!")
    #     print(questions[i])
    #     answer = input()

end = (counter / len(questions)) * 100

print(f"Вот и всё! Вы ответили на {counter} вопросов из {len(questions)} верно, это {end:.2f} процентов.")
