from termcolor import colored
import time


def mark_selection():
    print('¿Desea ser las X o los O? Escriba X/O')
    election = input()
    player = 'X'
    machine = 'O'
    if election == 'X' or election == 'x':
        return player, machine
    elif election == 'O' or election == 'o':
        player, machine = machine, player
        return player, machine
    else:
        print('Debe seleccionar una de las dos opciones')
        player, machine = mark_selection()
        return player, machine


def free_place(panel, line, column):
    return panel[line][column] == '*'


def line_question():
    print('¿En que fila desea escribir?')
    line = int(input())
    if line > 3 or line < 1:
        print('Recuerde que solo hay 3 lineas para elegir')
        line = line_question()
    return line


def column_question():
    print('¿En que columna desea escribir?')
    column = int(input())
    if column > 3 or column < 1:
        print('Recuerde que solo hay 3 columna para elegir')
        column = column_question()
    return column


def player_move():
    line = int(line_question())
    column = int(column_question())
    if free_place(board, line - 1, column - 1):
        board[line - 1][column - 1] = player_mark
    else:
        print('Esa posición esta ocupada, debe elegir otra ')
        player_move()
    print_board()


def machine_move():
    for i in range(3):
        for j in range(3):
            if board[i][j] == '*':
                board[i][j] = machine_mark
                print_board()
                return


def print_board():
    for i in range(3):
        for j in range(3):
            if board[i][j] == player_mark:
                print(colored(f' {player_mark} ', 'red'), end='')
            elif board[i][j] == machine_mark:
                print(colored(f' {machine_mark} ', 'blue'), end='')
            else:
                print(f' {board[i][j]} ', end='')
        print()


def winner(a, b):
    if a == 4 and b == 4:
        print('Empate!')
    elif board[a][b] == player_mark:
        print('Has ganado!!')
    elif board[a][b] == machine_mark:
        print('Lo siento, te gané!')


def game_end(panel):
    for i in range(3):
        # comprobar lineas
        if panel[i][0] == panel[i][1] and panel[i][1] == panel[i][2] and panel[i][0] != '*':
            return True, i, 0
        # comprobar columnas
        if panel[0][i] == panel[1][i] and panel[1][i] == panel[2][i] and panel[0][i] != '*':
            return True, 0, i
    # comprobar diagonal principal
    if panel[0][0] == panel[1][1] and panel[1][1] == panel[2][2] and panel[0][0] != '*':
        return True, 1, 1
        # comprobar diagonal opuesta
    if panel[0][2] == panel[1][1] and panel[1][1] == panel[2][0] and panel[0][2] != '*':
        return True, 1, 1

    # comprobar si esta completo
    for i in range(3):
        for j in range(3):
            if board[i][j] == '*':
                return False, 0, 0

    return True, 4, 4


print('Hola, bienvenido al Tres en raya, ¿Cual es su nombre? ')
name = input()
print(f'Hola {name}')

board = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

player_mark, machine_mark = mark_selection()
print('Perfecto, tu serás ' + colored(f'{player_mark}', 'red') + ' y yo seré ' +
      colored(f'{machine_mark}', 'blue') + ', ¿Desea empezar? S/N')
answer = input()

if answer == 'n' or answer == 'N':
    print('Pues empiezo yo ')
    machine_move()
elif answer == 's' or answer == 'S':
    print_board()

game = False
lin = 0
col = 0
while not game:
    player_move()
    game, lin, col = game_end(board)
    if not game:
        print("Pensando...")
        time.sleep(1)
        machine_move()
        game, lin, col = game_end(board)

winner(lin, col)
