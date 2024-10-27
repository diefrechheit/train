questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

counter = 0
counter_answer = 0

while True:
    welcome = input("Привет!\nПредлагаю проверить свои знания английского!\nНаберите 'ready', чтобы начать!\n")
    if welcome == "ready":
        break
    else:
        print("Кажется, вы не хотите играть. Очень жаль. Удачи")
        break

for i in range(len(questions)):
    print(questions[i])
    answer = input()
    if answer == answers[i]:
        print("Ответ верный!")
        counter += 1
        counter_answer += 1
    else:
        print(f"Неправильно. Правильный ответ: {answers[i]}")

end = (counter * counter_answer ** 3) / 100

print(f"Вот и всё! Вы ответили на {counter} вопросов из {counter_answer} верно, это {end} процентов.")
