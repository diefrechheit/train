# name = input("Привет! Предлагаю проверить свои знания английского, Напиши, как тебя зовут.")
# print(f"Привет, {name}, начинаем тренировку!")
#
# #Это счетчики баллов и ответов
# counter = 0
# counter_answer = 0
#
# #Решебник
# answer_1 = "is"
# answer_2 = "am"
# answer_3 = "in"
#
# #Первый вопрос
# first_questions = input("Вопрос 1: My name ____ Temiks\n")
# if first_questions == answer_1:
#     counter += 10
#     counter_answer += 1
#     print(f"Ответ верный!\nВы получаете {counter} баллов!")
# else:
#     print(f"Неправильно.\nПравильный ответ {answer_1}.")
#
# #Второй вопрос
# two_questions = input("Вопрос 2: I ____ a coder.\n")
# if two_questions == answer_2:
#     counter += 10
#     counter_answer += 1
#     print(f"Ответ верный!\nВы получаете {counter} баллов!")
# else:
#     print(f"Неправильно.\nПравильный ответ {answer_2}.")
#
# #Третий вопрос
# three_question = input("Вопрос 3: I live ____ Zatulinka\n")
# if three_question == answer_3:
#     counter += 10
#     counter_answer += 1
#     print(f"Ответ верный!\nВы получаете {counter} баллов!")
# else:
#     print(f"Неправильно.\nПравильный ответ {answer_3}.")
#
# #Процент
# finish = (counter_answer / 3) * 100
#
# print(
#     f'Вот и всё, {name}!\nВы ответили на {counter_answer} из 3 верно.\nВы заработали {counter} баллов.\n  Это {finish}%')