class Matrix:
    """
    Класс для представления матрицы с методами вывода и умножения.
    Как задать матрицу, пример:
        m1 = Matrix(2, 3)
        m1.data = [[1, 2, 3], [4, 5, 6]]
        Пример 2:
        m_data = [[1, 2, 3], [4, 5, 6]]
        m1 = Matrix(2, 3, m_data)
    """

    def __init__(self, rows: int, columns: int, data: list = None):
        self.rows = rows
        self.columns = columns
        if not data:
            self.data = []
        else:
            self.data = data

    def __str__(self):
        return '\n'.join('\t'.join(str(item) for item in row) for row in self.data) + '\n'

    def add(self, other):
        """
        Сложение матриц.
        :param other: Другая матрица.
        :return: Печатает результат сложения матриц.
        """
        if other.rows == self.rows and other.columns == self.columns:
            new_matrix = []
            for i in range(self.rows):
                new_row = []
                for j in range(self.columns):
                    new_row.append(self.data[i][j] + other.data[i][j])
                new_matrix.append(new_row)
            return '\n'.join('\t'.join(str(item) for item in row) for row in new_matrix) + '\n'
        else:
            raise ValueError('Матрицы разного размера, вычитание невозможно.')

    def subtract(self, other):
        """
        Вычитание матриц.
        :param Другая матрица.
        :return: Печатает результат вычитания матриц.
        """
        if other.rows == self.rows and other.columns == self.columns:
            new_matrix = []
            for i in range(self.rows):
                new_row = []
                for j in range(self.columns):
                    new_row.append(self.data[i][j] - other.data[i][j])
                new_matrix.append(new_row)
            return '\n'.join('\t'.join(str(item) for item in row) for row in new_matrix) + '\n'
        else:
            raise ValueError('Матрицы разного размера, вычитание невозможно.')

    def multiply(self, other):
        """
        Умножение матриц.
        :param other: Другая матрица.
        :return: Печатает результат перемножения матриц.
        """
        if self.columns == other.rows:
            new_matrix = []
            for i in range(self.rows):
                new_row = []
                for j in range(other.columns):
                    result = 0
                    for k in range(self.columns):
                        result += self.data[i][k] * other.data[k][j]
                    new_row.append(result)
                new_matrix.append(new_row)
            return '\n'.join('\t'.join(str(item) for item in row) for row in new_matrix) + '\n'
        else:
            raise ValueError('Нельзя перемножить матрицы: число столбцов первой не равно числу строк второй.')

    def transpose(self):
        new_matrix = []
        for i in range(self.columns):
            new_row = []
            for j in range(self.rows):
                new_row.append(self.data[j][i])
            new_matrix.append(new_row)
        return '\n'.join('\t'.join(str(item) for item in row) for row in new_matrix) + '\n'

# Примеры работы с классом:

# Создание экземпляров класса Matrix
m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

# Тестирование операций
print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
print(m1.add(m2))

print("Вычитание матриц:")
print(m1.subtract(m2))

m3_data = [[1, 2], [3, 4], [5, 6]]
m3 = Matrix(3, 2, m3_data)

print("Умножение матриц:")
print(m1.multiply(m3))

print("Транспонирование матрицы 1:")
print(m1.transpose())
