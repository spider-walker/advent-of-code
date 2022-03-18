import os

filename = os.path.dirname(__file__) + "\\input"
boards = []
drawn_numbers = []

with open(filename) as file:
    x = 0
    board_rows = []
    board_idx = 0
    for line in file:
        if x == 0:
            drawn_numbers = list(map(int, line.rstrip().split(','), ))
        else:
            if line.rstrip() == '':
                board_rows = []
                board_idx += 1
                boards.append(board_rows)
            else:
                board_rows.append(list(map(int, list(filter(None, line.rstrip().split(' ')))), ))
        x += 1


for x in range(5, len(drawn_numbers) + 1, 1):
    drawn_number = (drawn_numbers[0:x])
    board_idx = 0
    for board in boards:
        y = 0
        board_won = False
        'label'
        for b in board:
            lst2 = [item[y] for item in board]
            resultA = sum(el in b for el in drawn_number)
            resultB = sum(el in lst2 for el in drawn_number)
            if resultA == 5 or resultB == 5:
                score = (drawn_number[len(drawn_number) - 1])
                winning_board = sum(board, [])
                mj = list(set(winning_board) - set(drawn_number))
                results = sum(mj)
                print(f'{score} {resultA}  {results * score} {b}')
                boards.pop(board_idx)
                break
            y += 1
        board_idx += 1
