# задание_1


class Matrix:
    def __init__(self, data):
        self.input = data

    def __str__(self):
        return '\n'.join([' '.join([str(element) for element in line]) for line in self.input])

    def __add__(self, other):
        answer = ''
        if len(self.input) == len(other.input):
            for line_1, line_2 in zip(self.input, other.input):
                if len(line_1) != len(line_2):
                    return 'Разные размеры матриц'

                summed_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join([str(i) for i in summed_line]) + '\n'
        else:
            return 'Разные размеры матриц'
        return answer


matrix_1 = Matrix([[1, 4, 2], [1, 0, 5], [5, 2, 1]])
matrix_2 = Matrix([[3, 1, 4], [7, 2, 2], [0, 1, 0]])

print(matrix_1)
print()
print(matrix_1 + matrix_2)
