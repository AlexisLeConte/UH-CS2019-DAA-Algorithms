def _board_tiling(board, offset_x, offset_y, size, tile_x, tile_y, color):
    """L-shapes board tiling algorithm."""

    next_color = color + 1
    if size == 2:
        for i in range(offset_x, offset_x + size):
            for j in range(offset_y, offset_y + size):
                if board[i][j] == -1:
                    board[i][j] = color
        return next_color

    cut_x = offset_x + size // 2
    cut_y = offset_y + size // 2

    if tile_x < cut_x and tile_y < cut_y:
        next_color = _board_tiling(board, offset_x, offset_y, size // 2, tile_x, tile_y, next_color)
    else:
        board[cut_x - 1][cut_y - 1] = color
        next_color = _board_tiling(board, offset_x, offset_y, size // 2, cut_x - 1, cut_y - 1, next_color)

    if tile_x >= cut_x and tile_y < cut_y:
        next_color = _board_tiling(board, cut_x, offset_y, size // 2, tile_x, tile_y, next_color)
    else:
        board[cut_x][cut_y - 1] = color
        next_color = _board_tiling(board, cut_x, offset_y, size // 2, cut_x, cut_y - 1, next_color)

    if tile_x < cut_x and tile_y >= cut_y:
        next_color = _board_tiling(board, offset_x, cut_y, size // 2, tile_x, tile_y, next_color)
    else:
        board[cut_x - 1][cut_y] = color
        next_color = _board_tiling(board, offset_x, cut_y, size // 2, cut_x - 1, cut_y, next_color)

    if tile_x >= cut_x and tile_y >= cut_y:
        next_color = _board_tiling(board, cut_x, cut_y, size // 2, tile_x, tile_y, next_color)
    else:
        board[cut_x][cut_y] = color
        next_color = _board_tiling(board, cut_x, cut_y, size // 2, cut_x, cut_y, next_color)

    return next_color

def board_tiling(size, tile_x, tile_y):
    """L-shapes board tiling algorithm caller."""

    board = [[-1] * size for i in range(size)]
    board[tile_x][tile_y] = 0
    _board_tiling(board, 0, 0, len(board), tile_x, tile_y, 1)
    return board
