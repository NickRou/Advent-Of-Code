from typing import List

next_letters: dict = {
    'X': 'M',
    'M': 'A',
    'A': 'S',
}

def parse_input(filename: str) -> List[str]:
    with open(filename, 'r') as f:
        ret_val = f.read().splitlines()
    f.close()
    return ret_val

def xmas_word_search(word_search: List[str]) -> int:
    """Find all occurrences of XMAS in the word search"""
    xmas_word_total: int = 0
    for i in range(len(word_search)):
        for j in range(len(word_search[i])):
            curr_letter: str = word_search[i][j]
            if curr_letter == 'X':
                xmas_word_total += get_xmas_word_count(word_search, 'X', i, j, 0, 0)

    return xmas_word_total


def get_xmas_word_count(word_search: List[str], curr_letter: str, x, y, dir_x, dir_y) -> int:
    if x < 0 or x >= len(word_search) or y < 0 or y >= len(word_search[x]):
        return 0
    elif word_search[x][y] != curr_letter:
        return 0
    elif word_search[x][y] == 'S':
        return 1
    else:
        next_letter: str = next_letters[curr_letter]
        if dir_x == 0 and dir_y == 0:
            return (
                    get_xmas_word_count(word_search, next_letter, x + 1, y, 1, 0) +
                    get_xmas_word_count(word_search, next_letter, x - 1, y, -1, 0) +
                    get_xmas_word_count(word_search, next_letter, x, y + 1, 0, 1) +
                    get_xmas_word_count(word_search, next_letter, x, y - 1, 0, -1) +
                    get_xmas_word_count(word_search, next_letter, x - 1, y - 1, -1, -1) +
                    get_xmas_word_count(word_search, next_letter, x - 1, y + 1, -1, 1) +
                    get_xmas_word_count(word_search, next_letter, x + 1, y - 1, 1, -1) +
                    get_xmas_word_count(word_search, next_letter, x + 1, y + 1, 1, 1)
            )
        else:
            return get_xmas_word_count(word_search, next_letter, x + dir_x, y + dir_y, dir_x, dir_y)


def x_mas_word_search(word_search: List[str]) -> int:
    """
    Find all occurrences of XMAS in the word search
    M.S
    .A.
    M.S
    """

    xmas_word_total: int = 0
    for i in range(1, len(word_search)-1):
        for j in range(1, len(word_search[i])-1):
            curr_letter: str = word_search[i][j]
            if curr_letter == 'A':
                try:
                    left_diagonal_mas_exists = (
                            (word_search[i-1][j-1] == 'M' and word_search[i+1][j+1] == 'S') or
                            (word_search[i-1][j-1] == 'S' and word_search[i+1][j+1] == 'M')
                    )
                    right_diagonal_mas_exists = (
                            (word_search[i-1][j+1] == 'M' and word_search[i+1][j-1] == 'S') or
                            (word_search[i-1][j+1] == 'S' and word_search[i+1][j-1] == 'M')
                    )
                    if left_diagonal_mas_exists and right_diagonal_mas_exists:
                        xmas_word_total += 1
                except IndexError:
                    pass

    return xmas_word_total





if __name__=='__main__':
    day4_input = parse_input('day4.input')
    total = x_mas_word_search(day4_input)
    print("x_mas_word_total: " + str(total))