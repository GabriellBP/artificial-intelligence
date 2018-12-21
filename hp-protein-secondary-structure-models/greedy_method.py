import numpy as np


def count_seq_h(sequence, sequence_size):
    h = 0
    for i in range(1, sequence_size):
        if sequence[i] == 'H' and sequence[i-1] == 'H':
            h += 1
    return h


def count_mat_h(matrix, current_x, current_y):
    h = 0
    if matrix[current_x - 1][current_y] == 'H':
        h += 1
    if matrix[current_x][current_y - 1] == 'H':
        h += 1
    if matrix[current_x + 1][current_y] == 'H':
        h += 1
    if matrix[current_x][current_y + 1] == 'H':
        h += 1
    return h


def generate_possible_moviments(matrix, current_x, current_y):
    possible_moviments = []
    if matrix[current_x + 1][current_y] == '':
        possible_moviments.append('R')
    if matrix[current_x][current_y + 1] == '':
        possible_moviments.append('T')
    if matrix[current_x - 1][current_y] == '':
        possible_moviments.append('L')
    if matrix[current_x][current_y - 1] == '':
        possible_moviments.append('B')
    return possible_moviments


def greedy(matrix, matrix_size, sequence):
    current_y = current_x = int(matrix_size / 2)
    first_value = sequence.pop(0)
    matrix[current_x][current_y] = first_value

    qtd_h = 0

    while len(sequence) > 0:
        possible_moviments = generate_possible_moviments(matrix, current_x, current_y)
        if len(possible_moviments) == 0:
            print('CAIU NA TRAP')
            return 404  # not found :)
        value = sequence.pop(0)
        better_h = 0

        if value == 'H':
            h = 0
            for mov in possible_moviments.copy():
                if mov == 'R':
                    h = count_mat_h(matrix, current_x + 1, current_y)
                elif mov == 'L':
                    h = count_mat_h(matrix, current_x - 1, current_y)
                elif mov == 'T':
                    h = count_mat_h(matrix, current_x, current_y + 1)
                elif mov == 'B':
                    h = count_mat_h(matrix, current_x, current_y - 1)

                if h > better_h:
                    better_h = h
                    possible_moviments = [mov]
                elif h == better_h:
                    possible_moviments.append(mov)

        movement = possible_moviments[np.random.randint(0, len(possible_moviments))]
        if movement == 'L':
            current_x -= 1
        elif movement == 'R':
            current_x += 1
        elif movement == 'T':
            current_y += 1
        elif movement == 'B':
            current_y -= 1

        qtd_h += better_h
        matrix[current_x][current_y] = value

    return qtd_h


def main():
    sequences = ['HPHPPHHPHPPHPHHPPHPH',
                 'HHPPHPPHPPHPPHPPHPPHPPHH',
                 'PPHPPHHPPPPHHPPPPHHPPPPHH',
                 'PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP',
                 'PPHPPHHPPHHPPPPPHHHHHHHHHHPPPPPPHHPPHHPPHPPHHHHH',
                 'PPHPPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH']
    sequence = list(sequences[0])
    sequence_size = len(sequence)
    optimal_seq = count_seq_h(sequence, sequence_size)
    matrix_size = 2*sequence_size + 1  # never crosses a border
    # matrix = [['' for x in range(matrix_size)] for y in range(matrix_size)]
    matrix = np.array([''] * (matrix_size**2)).reshape((matrix_size, matrix_size))
    optimal = greedy(matrix, matrix_size, sequence.copy()) - optimal_seq
    print('-', optimal)


if __name__ == '__main__':
    main()
