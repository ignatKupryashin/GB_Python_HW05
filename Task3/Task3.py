# # 3. Создайте программу для игры в ""Крестики-нолики"".
#
# player = "X"
#
# field = []
# for i in range(4):
#     field.append([i, "", "", ""])
# field[0][1], field[0][2], field [0][3] = 1, 2, 3
#
#
# def change_player(player):
#     if player == "X":
#         player = "O"
#     else:
#         player = "X"
#     return player
#
# def show_field(field):
#     for i in range(4):
#         print(field[i])
#
# show_field(field)
#
#
# def check_winner(point):
#     winner = False
#     if field[point[0][1]] == field[point[0][2]] and field[point[0][1]] == field[point[0][3]]:
#         winner = True
#     if field[point[0][1]] == field[point[0][2]] and field[point[0][1]] == field[point[0][3]]:
#         sdf