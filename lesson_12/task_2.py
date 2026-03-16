class Matrix:
    def __init__(self, data:list) -> None:
        if not data or not all(isinstance(row, list) for row in data):
            raise ValueError("Матрица должна быть списком списков")
        row_len = len(data[0])
        if any(len(row) != row_len for row in data):
            raise ValueError("Все строки должны быть одинаковой длины")
        self.data = [row[:] for row in data]

    def rows(self) -> int:
        return len(self.data)

    def cols(self) -> int:
        return len(self.data[0])

    def size(self) -> tuple:
        return (self.rows(), self.cols())

    def __add__(self, other:Matrix) -> Matrix:
        if self.size() != other.size():
            raise ValueError("Матрицы должны быть одинакового размера")
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols())]
            for i in range(self.rows())
        ]
        return Matrix(result)

    def __sub__(self, other:Matrix) -> Matrix:
        if self.size() != other.size():
            raise ValueError("Матрицы должны быть одинакового размера")
        result = [
            [self.data[i][j] - other.data[i][j] for j in range(self.cols())]
            for i in range(self.rows())
        ]
        return Matrix(result)
    def __mul__(self, number: float) -> Matrix:
        if not isinstance(number, (int, float)):
            raise TypeError("Матрицу можно умножить только на число")
        result = [[x * number for x in row] for row in self.data]
        return Matrix(result)

    def transpose(self) -> Matrix:
        result = list(map(list, zip(*self.data)))
        return Matrix(result)

    def no_minus(self) -> Matrix:
        result = [[x if x >= 0 else 0 for x in row] for row in self.data]
        return Matrix(result)

    def count(self) -> int:
        return self.rows() * self.cols()

    def sum(self) -> float:
        return sum(sum(row) for row in self.data)

    def __eq__(self, other) -> bool:
        return self.data == other.data and isinstance(other, Matrix)

    def __str__(self) -> str:
        return "\n".join(" ".join(f"{x:6g}" for x in row) for row in self.data)

    @classmethod
    def zero(cls, m:int, n:int) -> Matrix:
        return cls([[0 for _ in range(n)] for _ in range(m)])

    @classmethod
    def one(cls, m:int, n:int) -> Matrix:
        return cls([[1 for _ in range(n)] for _ in range(m)])

    @classmethod
    def diagonal(cls, d_list:list[float]) -> Matrix:
        size = len(d_list)
        return cls([[d_list[i] if i == j else 0 for j in range(size)] for i in range(size)])


m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m)
print("\nБез отрицательных:")
print(m.no_minus())
print("\nТранспонирование:")
print(m.transpose())
print("\nСложение:")
print(m+m)
print("\nИз едениц:")
print(Matrix.one(3,3))
print("\nИз нулей:")
print(Matrix.zero(3,3))
print("\nДиагональная:")
print(Matrix.diagonal([5, 7, 2]))
