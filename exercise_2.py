from typing import List, Tuple


def queen_moves_num(n: int, r_q: int, c_q: int, obstacles: List[Tuple[int, int]]) -> int:
    """
    Calculates number of fields the queen can attack on the chessboard.
    :param n: size of the board
    :param r_q: row coordinate of the queen
    :param c_q: column coordinate of the queen
    :param obstacles: list of obstacle coordinates, that block the queen
    :return: number of fields the queen can attack
    """

    fields = 0  # number of fields the queen can attack

    queen_pos = (r_q - 1, c_q - 1)  # subtracting one, because the board is indexed from 1, not from 0
    queen_cor_sum = queen_pos[0] + queen_pos[1]
    queen_cor_diff = abs(queen_pos[0] - queen_pos[1])

    queen_left_border_distance = queen_pos[1]
    queen_right_border_distance = ((n - 1) - queen_pos[1])
    queen_upper_border_distance = ((n - 1) - queen_pos[0])
    queen_lower_border_distance = queen_pos[0]

    # careful with the indexing, again
    # "fixing" coordinates of obstacles where it's relevant

    # obstacles on the queen's row
    row_obstacles = [(obstacle[0] - 1, obstacle[1] - 1) for obstacle in obstacles if obstacle[0] - 1 == queen_pos[0]]

    # obstacles on the queen's column
    col_obstacles = [(obstacle[0] - 1, obstacle[1] - 1) for obstacle in obstacles if obstacle[1] - 1 == queen_pos[1]]

    # obstacle is on the same \ shaped diagonal as the queen, if:
    # the sum of the coordinates matches

    desc_diagonal_obstacles = [(obstacle[0] - 1, obstacle[1] - 1) for obstacle in obstacles if
                               (obstacle[0] - 1) + (obstacle[1] - 1) == queen_cor_sum]

    # obstacle is on the same / shaped diagonal as the queen, if:
    # the absolute difference of the coordinates matches

    asc_diagonal_obstacles = [(obstacle[0] - 1, obstacle[1] - 1) for obstacle in obstacles if
                              abs((obstacle[0] - 1) - (obstacle[1] - 1)) == queen_cor_diff
                              # if both conditions are true, it's on the \ diagonal
                              and (obstacle[0] - 1, obstacle[1] -1) not in desc_diagonal_obstacles]

    if row_obstacles:  # if there is at least one obstacle on the same row as the queen
        # check fields to the right

        right_obstacle_cols = [obstacle[1] for obstacle in row_obstacles if obstacle[1] > queen_pos[1]]
        if right_obstacle_cols:  # if there is at least one obstacle to the right:
            closest_obstacle_col = min(right_obstacle_cols)
            fields += ((closest_obstacle_col - queen_pos[1])-1)  # add number of fields between queen and obstacle
        else:
            fields += queen_right_border_distance  # add number of fields between queen and right side border

        # check fields to the left

        left_obstacle_cols = [obstacle[1] for obstacle in row_obstacles if obstacle[1] < queen_pos[1]]
        if left_obstacle_cols:  # if there is at least one obstacle to the left:
            closest_obstacle_col = max(left_obstacle_cols)
            fields += ((queen_pos[1] - closest_obstacle_col)-1)  # add number of fields between queen and obstacle
        else:
            fields += queen_left_border_distance  # add number of fields between queen and left side border
            # (this is equal to queen column coordinate)
    else:
        fields += (n - 1)  # add entire row (except 1, the queen's field) to available fields

    if col_obstacles:  # if there is at least one obstacle on the same column as the queen
        # check fields above

        above_obstacle_rows = [obstacle[0] for obstacle in col_obstacles if obstacle[0] > queen_pos[0]]
        if above_obstacle_rows:  # if there is at least one obstacle above:
            closest_obstacle_row = min(above_obstacle_rows)
            fields += ((closest_obstacle_row - queen_pos[0])-1)  # add number of fields between queen and obstacle
        else:
            fields += queen_upper_border_distance  # add number of fields between queen and upper border

        # check fields below

        below_obstacle_rows = [obstacle[0] for obstacle in col_obstacles if obstacle[0] < queen_pos[0]]
        if below_obstacle_rows:  # if there is at least one obstacle below:
            closest_obstacle_row = max(below_obstacle_rows)
            fields += ((queen_pos[0] - closest_obstacle_row)-1)  # add number of fields between queen and obstacle
        else:
            fields += queen_lower_border_distance  # add number of fields between queen and lower border
            # (this is equal to the queen row coordinate)
    else:
        fields += (n - 1)  # add entire column (except 1, the queen's field) to available fields

    if desc_diagonal_obstacles:  # if there is at least one obstacle on the same \ diagonal as the queen:
        # check fields above

        above_obstacle_rows = [obstacle[0] for obstacle in desc_diagonal_obstacles if obstacle[0] > queen_pos[0]]
        if above_obstacle_rows:  # if there is at least one obstacle above:
            closest_obstacle_row = min(above_obstacle_rows)
            fields += ((closest_obstacle_row - queen_pos[0])-1)  # add number of fields between queen and obstacle
        else:
            # add number of fields between queen and upper border or left border, whichever is closer
            fields += min(queen_upper_border_distance, queen_left_border_distance)

        # check fields below

        below_obstacle_rows = [obstacle[0] for obstacle in desc_diagonal_obstacles if obstacle[0] < queen_pos[0]]
        if below_obstacle_rows:  # if there is at least one obstacle below:
            closest_obstacle_row = max(below_obstacle_rows)
            fields += ((queen_pos[0] - closest_obstacle_row)-1)  # add number of fields between queen and obstacle
        else:
            # add number of fields between queen and lower border or right border, whichever is closer
            fields += min(queen_lower_border_distance, queen_right_border_distance)
    else:
        # add entire \ diagonal
        fields += min(queen_upper_border_distance, queen_left_border_distance) \
                  + min(queen_lower_border_distance, queen_right_border_distance)

    if asc_diagonal_obstacles:  # if there is at least one obstacle on the same / diagonal as the queen:
        # check fields above

        above_obstacle_rows = [obstacle[0] for obstacle in asc_diagonal_obstacles if obstacle[0] > queen_pos[0]]
        if above_obstacle_rows:  # if there is at least one obstacle above:
            closest_obstacle_row = min(above_obstacle_rows)
            fields += ((closest_obstacle_row - queen_pos[0])-1)  # add number of fields between queen and obstacle
        else:
            # add number of fields between queen and upper border or right border, whichever is closer
            fields += min(queen_upper_border_distance, queen_right_border_distance)

        # check fields below

        below_obstacle_rows = [obstacle[0] for obstacle in asc_diagonal_obstacles if obstacle[0] < queen_pos[0]]
        if below_obstacle_rows:  # if there is at least one obstacle below:
            closest_obstacle_row = max(below_obstacle_rows)
            fields += ((queen_pos[0] - closest_obstacle_row)-1)  # add number of fields between queen and obstacle
        else:
            # add number of fields between queen and lower border or left border, whichever is closer
            fields += min(queen_lower_border_distance, queen_left_border_distance)
    else:
        # add entire / diagonal
        fields += min(queen_upper_border_distance, queen_right_border_distance) \
                  + min(queen_lower_border_distance, queen_left_border_distance)
    return fields
