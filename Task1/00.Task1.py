# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open("01.text.txt", "r") as file:
    initial_text = file.read()

question = "абв"

final_text = list(filter(lambda x: question not in x, initial_text.split(" ")))
final_text = " ".join(final_text)

with open("02.answer.txt", "w") as file:
    file.write(final_text)