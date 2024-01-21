# Создаем список из девяти элементов, которые будут представлять сетку игры
val = [' ' for i in range(9)]


# Создаем функцию, которая будет выводить сетку игры на экран
def print_board():
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(val[0], val[1], val[2]))
    print('\t_____|_____|_____')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(val[3], val[4], val[5]))
    print('\t_____|_____|_____')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(val[6], val[7], val[8]))
    print("\t     |     |")
    print("\n")


# Создаем функцию, которая будет проверять, есть ли победитель в игре
def check_winner():
    # Проверяем горизонтальные линии
    if val[0] == val[1] == val[2] != ' ':
        return val[0]
    if val[3] == val[4] == val[5] != ' ':
        return val[3]
    if val[6] == val[7] == val[8] != ' ':
        return val[6]
    # Проверяем вертикальные линии
    if val[0] == val[3] == val[6] != ' ':
        return val[0]
    if val[1] == val[4] == val[7] != ' ':
        return val[1]
    if val[2] == val[5] == val[8] != ' ':
        return val[2]
    # Проверяем диагональные линии
    if val[0] == val[4] == val[8] != ' ':
        return val[0]
    if val[2] == val[4] == val[6] != ' ':
        return val[2]
    # Если нет победителя, возвращаем None
    return None


# Создаем функцию, которая будет проверять, есть ли свободные клетки в сетке игры
def is_board_full():
    return ' ' not in val


# Создаем функцию, которая будет запрашивать у игрока ввод числа от 1 до 9
def get_player_move(player):
    while True:
        move = input(f"Игрок {player}, введите число от 1 до 9: ")
        if move.isdigit() and 1 <= int(move) <= 9:
            move = int(move) - 1
            if val[move] == ' ':
                return move
            else:
                print("Эта клетка уже занята, выберите другую.")
        else:
            print("Неверный ввод, попробуйте еще раз.")


# Создаем функцию, которая будет менять очередность игроков
def switch_player(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'


# Создаем функцию, которая будет реализовывать основной цикл игры
def play_game():
    # Определяем начального игрока
    player = 'X'
    # Выводим пустую сетку игры
    print_board()
    # Повторяем, пока игра не закончится
    while True:
        # Получаем ход игрока
        move = get_player_move(player)
        # Заполняем клетку сетки символом игрока
        val[move] = player
        # Выводим обновленную сетку игры
        print_board()
        # Проверяем, есть ли победитель
        winner = check_winner()
        if winner is not None:
            print(f"Игрок {winner} победил!")
            break
        # Проверяем, есть ли ничья
        if is_board_full():
            print("Ничья!")
            break
        # Меняем очередность игрока
        player = switch_player(player)


# Запускаем игру
play_game()
