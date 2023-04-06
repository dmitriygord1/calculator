# Создаем пустое поле 3х3
field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# Функция для вывода поля в консоль
def print_field():
    print('  1 2 3')
    print(' +-+-+-+')
    for i in range(3):
        print(f'{i+1}|{field[i][0]}|{field[i][1]}|{field[i][2]}|')
        print(' +-+-+-+')

# Функция для проверки выигрышной комбинации
def check_win(player):
    # Проверяем по горизонтали
    for i in range(3):
        if field[i][0] == player and field[i][1] == player and field[i][2] == player:
            return True
    # Проверяем по вертикали
    for j in range(3):
        if field[0][j] == player and field[1][j] == player and field[2][j] == player:
            return True
    # Проверяем по диагонали
    if field[0][0] == player and field[1][1] == player and field[2][2] == player:
        return True
    if field[0][2] == player and field[1][1] == player and field[2][0] == player:
        return True
    return False

# Главный цикл игры
current_player = 'X'
while True:
    # Выводим поле и просим игрока сделать ход
    print_field()
    row = int(input(f'Игрок {current_player}, введите номер строки (1-3): '))
    col = int(input(f'Игрок {current_player}, введите номер столбца (1-3): '))
    # Проверяем, что выбранные координаты находятся в диапазоне 1-3
    if row < 1 or row > 3 or col < 1 or col > 3:
        print('Неверные координаты!')
        continue
    # Проверяем, что выбранная клетка пустая
    if field[row-1][col-1] != ' ':
        print('Эта клетка уже занята!')
        continue
    # Записываем ход игрока на поле
    field[row-1][col-1] = current_player
    # Проверяем, не выиграл ли игрок
    if check_win(current_player):
        print_field()
        print(f'Игрок {current_player} выиграл!')
        break
    # Проверяем, не закончилась ли игра в ничью
    if all([cell != ' ' for row in field for cell in row]):
        print_field()
        print('Ничья!')
        break
    # Переключаем текущего игрока
    current_player = 'O' if current_player == 'X' else 'X'