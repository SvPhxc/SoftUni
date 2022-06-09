def build_initial_field(rows_count, columns_count):
    return [[None] * columns_count for _ in range(rows_count)]


def get_cell_value(cell):
    return cell if cell else 0


def print_field(field):
    [print(row) for row in field]

def print_winner(player):
    print(f"PLayer {player} wins!")

def get_player_move(player):
    player_move_str = input(f'PLayer {player}, please choose a column!')
    player_move = int(player_move_str)
    return player_move - 1

def apply_player_move_gen(rows_count, columns_count):
    free_bottom_row_indices = [rows_count - 1] * columns_count
    def apply_player_move_internal(player, player_move, field):
        player_row = free_bottom_row_indices[player_move]
        field[player_row][player_move] = player
        free_bottom_row_indices[player_move] -= 1

    return apply_player_move_internal





def is_win_condition(player, player_row, player_column, field):
    def is_win_condition_in_direction(field, row, column, direction):
        row_delta, column_delta = direction
        row_boundary = min(len(field), row + 4 * direction)
        columns_boundary = min(len(field[0]), column + 4 * direction)
        counter = 0

        is_row_included = row_boundary == row
        is_column_included = columns_boundary == row

        while (row != row_boundary or is_row_included) \
                and (column != columns_boundary or is_column_included) \
                and player == field[row][column]:
            counter += 1
            row += row_delta
            column += column_delta

        return counter == 4


    directions = [
        (0, 1),
        (1, 0),
        (1, 1),
        (-1, 1)
    ]
    return any(is_win_condition_in_direction(field, player_row, player_column, direction) for direction in directions)


def play(field):
    rows_count = len(field)
    columns_count = len(field[0])
    apply_player_move = apply_player_move_gen(rows_count, columns_count)
    current_player, other_player = 1, 2

    while True:
        player_move = get_player_move(current_player)
        apply_player_move(current_player, player_move, field)
        # if is_win_condition():
        #     break
        # else:
        #     current_player, other_player = other_player, current_player
        print_field(field)
    # print_winner(current_player)




# field = build_initial_field(6, 7)
# play(field)
