class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = self.string_to_matrix(matrix_string)
        pass

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [row[index-1] for row in self.matrix]

    def string_to_matrix(self, matrix_string):
        rows = matrix_string.splitlines()
        return [list(map(int, row.split())) for row in rows]
