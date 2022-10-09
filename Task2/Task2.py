# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
#

candies = int(100)
current_player = "player1"

names = {"player1": input("Введите ваше имя: "), "player2": "Бездушный компьютер"}


def change_player(player): # Метод для смены игрока
    if player == "player1":
        player = "player2"
    else:
        player = "player1"
    return player


def move(player, current_candies): # Метод хода игрока
    print(f"Ход игрока {names[player]}")
    print(f"Сейчас на столе {current_candies} конфет")
    current_move = input("Сколько конфет вы берёте? (от 1 до 28):")
    if current_move.isdigit():
        current_move = int(current_move)
    else:
        print("Нужно ввести число цифрами")
        return move(player, current_candies)
    if 0 < current_move <= 28 and current_move <= current_candies:
        return current_candies - current_move
    else:
        print("Невозможно взять столько конфет")
        return move(player, current_candies)


while True:
    candies = move(current_player, candies)
    if candies == 0:
        print(f"Победил {names[current_player]}")
        break
    else:
        current_player = change_player(current_player)