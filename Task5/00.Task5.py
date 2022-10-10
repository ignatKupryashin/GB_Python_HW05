# # 5*. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open("01.question.txt", "r") as file:
    my_list = list(file.read().split(", "))

print(f"Изначальная последовательность: {my_list}")


# def increase_sequence(some_list):


def next_sequence(some_list, current_sequence=[], coordinate=0):
    print(coordinate)
    if (coordinate == len(some_list) - 1):
        return
    current_sequence.append(some_list[coordinate])
    for i in range(coordinate, len(some_list)):
        for j in range(coordinate + 1, len(some_list)):
            if int(some_list[coordinate]) < int(some_list[j]):
                next_sequence(some_list, current_sequence, j)
                # print(current_sequence)
    print("Дошло до ответа")
    # print(current_sequence)
    return
#

next_sequence(my_list)

# def next_sequence(some_list, answer, current_sequence = []):
#
#     for i in range(len(some_list)):
#         current_sequence.append(some_list[i])
#         for j in range(i + 1, len(some_list)):
#             if some_list[i] < some_list[j]:
#                 current_sequence.append(some_list[j])
#                 answer.append(some_list[j])
#     return answer
#

# some_answer = next_sequence(my_list, [])

# n = 1
# for r in range(len(some_answer)):
#     print(f"{n}: {some_answer[r]}")
#     n += 1

# current = []
# answer = []
# current.append("1")
# somecopy = current.copy()
# answer.append(somecopy)
# print(answer)
# current.append("3")
# print(answer)
# somecopy = current.copy()
# answer.append(somecopy)
# print(answer)
