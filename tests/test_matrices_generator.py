import unittest
from matrices_workers import MatricesGenerator


def check_matrix_values(matrix: list, data: dict) -> bool:
    return all([data['min_value'] <= elem <= data['max_value'] for i in range(len(matrix)) for elem in matrix[i]])


class TestMatricesGenerator(unittest.TestCase):

    def test_generate_matrix_case_1(self):
        data = dict(min_value=-10, max_value=10, height=5, width=5)
        matrices_generator = MatricesGenerator(**data)
        matrix = matrices_generator._generate_matrix()
        self.assertEqual(len(matrix), data['height'])
        self.assertEqual(len(matrix[0]), data['width'])
        self.assertEqual(check_matrix_values(matrix, data), True)

    def test_generate_matrix_case_2(self):
        data = dict(min_value=-999, max_value=999, height=20, width=20)
        matrices_generator = MatricesGenerator(**data)
        matrix = matrices_generator._generate_matrix()
        self.assertEqual(len(matrix), data['height'])
        self.assertEqual(len(matrix[0]), data['width'])
        self.assertEqual(check_matrix_values(matrix, data), True)

    def test_generate_matrix_case_3(self):
        data = dict(min_value=5, max_value=10, height=5, width=10)
        matrices_generator = MatricesGenerator(**data)
        matrix = matrices_generator._generate_matrix()
        self.assertEqual(len(matrix), data['height'])
        self.assertEqual(len(matrix[0]), data['width'])
        self.assertEqual(check_matrix_values(matrix, data), True)

    def test_generate_matrix_case_4(self):
        data = dict(min_value=-10, max_value=5, height=10, width=5)
        matrices_generator = MatricesGenerator(**data)
        matrix = matrices_generator._generate_matrix()
        self.assertEqual(len(matrix), data['height'])
        self.assertEqual(len(matrix[0]), data['width'])
        self.assertEqual(check_matrix_values(matrix, data), True)

    def test_generate_matrix_case_5(self):
        data = dict(min_value=1, max_value=1, height=1, width=1)
        matrices_generator = MatricesGenerator(**data)
        matrix = matrices_generator._generate_matrix()
        self.assertEqual(len(matrix), data['height'])
        self.assertEqual(len(matrix[0]), data['width'])
        self.assertEqual(check_matrix_values(matrix, data), True)

    def test_generate_matrices(self):
        data = dict(min_value=-10, max_value=10, height=3, width=3)
        matrices_generator = MatricesGenerator(**data)
        matrices = matrices_generator._generate_matrices()
        self.assertEqual(bool(matrices.get('matrix_1')), True)
        self.assertEqual(bool(matrices.get('matrix_2')), True)

