# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rle(string):
    length = len(string)
    pointer = 0
    answer = ""
    while pointer < length:
        counter = 1
        if pointer + counter >= length:
            break
        while string[pointer] == string[pointer + counter]:
            counter += 1
            if pointer + counter >= length:
                break
        if counter > 9:
            while counter > 9:
                answer += f"{string[pointer]}9"
                counter -= 9
                pointer = pointer + 9
        answer += f"{string[pointer]}{counter}"
        pointer = pointer + counter
    return answer

def un_rle(string):
    answer = ""
    for i in range(0, len(string), 2):
        number = int(string[i + 1])
        for j in range(number):
            answer += string[i]
    return answer

my_string = "aaaabbbbbbbbhhhhh222222333333aaaaaaaaaakkkk"
print(my_string)
new_string = rle(my_string)
print(new_string)
new_string = un_rle(new_string)
print(new_string)
print(my_string == new_string)



